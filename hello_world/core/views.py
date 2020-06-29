from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request):
    return HttpResponse('Hello World!')

def helloName(request, name):
    return HttpResponse('<h1>Hello {}!<h1>'.format(name))

def soma(request, num1, num2):
    return HttpResponse('<h1>{} + {} = {}</h1>'.format(num1, num2, num1+num2))
