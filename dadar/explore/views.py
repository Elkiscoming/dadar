from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.


def init(request, location):
    return HttpResponse("salam " + location)


def index(request):
    return render(request, 'explore/index.html')