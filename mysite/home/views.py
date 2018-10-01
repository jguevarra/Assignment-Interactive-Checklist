from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Welcome home, we've been expecting you!") 