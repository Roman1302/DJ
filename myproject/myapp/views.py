from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse (f"<h1>Привет от Романа!</h1>")


def about(request):
    return HttpResponse(f"<p>Я учусь программированию</p>")
# Create your views here.
