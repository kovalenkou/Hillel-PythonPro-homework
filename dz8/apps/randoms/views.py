from datetime import datetime
import random

from pickle import GET
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, CreateView


class randoms(CreateView):

    def get(self, request):
        return render(request, 'randoms/randoms.html', {})

    def post(self, request):
        length = int(request.POST.get('length'))
        specials = 1 if request.POST.get('specials') == 'on' else 0
        digits = 1 if request.POST.get('digits') == 'on' else 0
        res_string = ''
        if (length < 0 or length > 100) or specials not in (0, 1) or digits not in (0, 1):
            if length < 0 or length > 100:
                res_string += f"<p>Input {length} is not correct. Choose integer more than 0 and less then 100!</p>"
            if specials not in (0, 1):
                res_string += f'<p>Input specials: "{specials}" is not correct. Choose 0 or 1!</p>'
            if digits not in (0, 1):
                res_string += f'<p>Input digits: "{digits}" is not correct. Choose 0 or 1!</p>'
        else:
            chars_list = [chr(_) for _ in range(ord('A'), ord('Z')+1)]
            chars_list.extend([chr(_) for _ in range(ord('a'), ord('z') + 1)])
            if specials:
                chars_list.extend([chr(_) for _ in range(ord(' '), ord('/') + 1)])
            if digits:
                chars_list.extend([chr(_) for _ in range(ord('0'), ord('9') + 1)])
            res_string = ''.join(random.choices(chars_list, k=length))
        return render(request, 'randoms/randoms.html', {'res_string': res_string})
