from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def hello(request):

    return HttpResponse(66666)


def index(request):
    return render(request, 'index.html')
