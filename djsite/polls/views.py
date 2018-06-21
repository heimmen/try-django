# from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """The function's docstring"""
    return HttpResponse("Hello kitty, you are in the polls index.")
