from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request):
    return HttpResponse('Hello World!')

def helloName(request, name):
    return HttpResponse('<h1>Hello {}!<h1>'.format(name))