# dz-3 OOP amd magic methods

class Url:
    def __init__(self, scheme: str, authority: str = None,
                 path: list = None, query: dict = None, fragment: str = None
                 ):
        self.scheme = scheme
        self.authority = authority
        self.path = path
        self.query = query
        self.fragment = fragment

    def __str__(self):
        url_scheme = f'{self.scheme}:'
        url_authority = f'//{self.authority}' if self.authority else ''
        if self.path is None:
            url_path = ''
        else:
            url_path = '/' + '/'.join([x for x in self.path])
        if self.query is None:
            url_query = ''
        else:
            url_query1 = [f'{x[0]}={x[1]}' for x in self.query.items()]
            url_query = '?' + '&'.join(url_query1)
        url_fragment = f'#{self.fragment}' if self.fragment else ''
        return url_scheme + url_authority + url_path + url_query + url_fragment

    def __eq__(self, other):
        if str(self) == str(other):
            return True
        else:
            return False


class HttpUrl(Url):
    def __init__(self, authority=None, path=None, query=None, fragment=None):
        super().__init__('http', authority, path, query, fragment)


class HttpsUrl(Url):
    def __init__(self, authority=None, path=None, query=None, fragment=None):
        super().__init__('https', authority, path, query, fragment)


class GoogleUrl(HttpsUrl):
    def __init__(self, path=None, query=None, fragment=None):
        super().__init__('google.com', path, query, fragment)


class WikiUrl(HttpsUrl):
    def __init__(self, path=None, query=None, fragment=None):
        super().__init__('wikipedia.org', path, query, fragment)


class UrlCreator(Url):
    path_list = list()

    def __init__(self, scheme: str, authority: str = None):
        self.path_list.clear()
        super().__init__(scheme, authority, path=None, query=None, fragment=None)

    def __str__(self):
        url_string = super(UrlCreator, self).__str__()
        self.path_list.clear()
        return url_string

    def _create(self):
        return Url(self.scheme, self.authority, self.path, self.query, self.fragment)

    def __call__(self, *args, **kwargs):
        if len(args) != 0:
            self.path_list.clear()
            self.path_list = [_ for _ in args]
            self.__setattr__('path', self.path_list)
        if len(kwargs) != 0:
            self.__setattr__('query', kwargs)
        return self

    def __getattribute__(self, attr):
        return super(Url, self).__getattribute__(attr)

    def __getattr__(self, attr):
        self.path_list.append(attr)
        self.__setattr__('path', self.path_list)
        return self


if __name__ == '__main__':
    print('part 3')
    assert GoogleUrl() == HttpsUrl(authority='google.com')
    assert GoogleUrl() == Url(scheme='https', authority='google.com')
    assert GoogleUrl() == 'https://google.com'
    assert WikiUrl() == str(Url(scheme='https', authority='wikipedia.org'))
    assert WikiUrl(path=['wiki', 'python']) == 'https://wikipedia.org/wiki/python'
    assert GoogleUrl(query={'q': 'python', 'result': 'json'}) == 'https://google.com?q=python&result=json'

    url1 = Url('http', 'google.com')
    print(f'url1 = {str(url1)}')
    url2 = Url('https', 'google.com', ['dddd', 'aaaa', 'pppp'])
    print(f'url2 = {str(url2)}')
    url3 = Url('https', 'google.com', ['dddd', 'aaaa', 'pppp'], {'key1': 'value1', 'key2': 'value2'})
    print(f'url3 = {str(url3)}')
    url4 = Url('https', 'google.com', ['dddd', 'aaaa', 'pppp'], {'key1': 'value1', 'key2': 'value2'}, 'fragment')
    print(f'url4 = {str(url4)}')
    url5 = Url('https', 'google.com', query={'key1': 'value1', 'key2': 'value2'}, fragment='fragment')
    print(f'url5 = {str(url5)}')
    url6 = Url('https', 'google.com', ['dddd', 'aaaa', 'pppp'], fragment='fragment')
    print(f'url6 = {str(url6)}')
    url7 = Url('https', 'google.com', ['dddd', 'aaaa', 'pppp'], query={'key1': 'value1', 'key2': 'value2'})
    print(f'url7 = {str(url7)}')
    url8 = Url('http')
    print(f'If url8 = {str(url8)}')

    print(f"If {Url(scheme='https', authority='google.com') == 'https://google.com'}, than equal")

    print('\npart 4')
    url_creator = UrlCreator(scheme='https', authority='docs.python.org')
    assert url_creator.docs.v1.api.list == 'https://docs.python.org/docs/v1/api/list'
    assert url_creator('api', 'v1', 'list') == 'https://docs.python.org/api/v1/list'
    assert url_creator('api', 'v1', 'list', q='my_list') == 'https://docs.python.org/api/v1/list?q=my_list'

    assert url_creator('3').search(q='getattr', check_keywords='yes',
                                   area='default'
                                   )._create() == 'https://docs.python.org/3/search?q=getattr&check_keywords=yes&area=default',\
        "RRRRRRR"

    print(url_creator.docs.v1.api.list)
    print(url_creator.docs.v1.docs)
    print(url_creator('api', 'v1', 'list'))
    print(url_creator('api', 'v1', 'list', q='my_list'))
    print(url_creator('3').search(q='getattr', check_keywords='yes', area='default'))
    url1 = url_creator('3').search(q='getattr', check_keywords='yes', area='default')._create()
    print(f'url after _create() {url1}')
