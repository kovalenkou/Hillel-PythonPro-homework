from pickle import GET
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, CreateView


class index_page(CreateView):

    def get(self, request):
        return render(request, 'about/index_page.html', {})


class about(CreateView):

    def get(self, request):
        return render(request, 'about/about.html', {})


class whoami(CreateView):

    def get(self, request):
        # browser
        browser = request.META.get('HTTP_USER_AGENT')
        # ip
        ip_address = request.META.get('REMOTE_ADDR')
        # Current time on server
        current = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        return render(request, 'about/whoami.html', {'browser': browser, 'ip_address': ip_address, 'current': current})
