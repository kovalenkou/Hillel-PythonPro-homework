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
    print(f'url8 = {str(url8)}')

    print(Url(scheme='https', authority='google.com') == 'https://google.com')

    # print('part 4')
    # assert GoogleUrl() == HttpsUrl(authority='google.com')
    # assert GoogleUrl() == Url(scheme='https', authority='google.com')
    # assert GoogleUrl() == 'https://google.com'
    # assert WikiUrl() == str(Url(scheme='https', authority='wikipedia.org'))
    # assert WikiUrl(path=['wiki', 'python']) == 'https://wikipedia.org/wiki/python'))
    # assert GoogleUrl(query={'q': 'python', 'result': 'json'}) == 'https://google.com?q=python&result=json'))