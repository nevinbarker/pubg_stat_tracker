from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('userlogin/index.html')
    context = {
        'username': 'password'
    }
    return HttpResponse(template.render(context, request))

