from django.shortcuts import render
from django.http import HttpResponse


def address(request):
    return HttpResponse("Я проживаю в г. Сыктывкар Республика Коми")


def activity(request):
    return HttpResponse("Я занимаюсь здоровьем людей с помощью продукции компании Арт Лайф")
# Create your views here.
# Create your views here.
