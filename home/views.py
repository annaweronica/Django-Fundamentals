# from django.shortcuts import render
from django.http import HttpResponse


def landing_page(request):
    return HttpResponse('Well, this is my response to you request')


def another_page(request):
    return HttpResponse('Well, this is my for that url')