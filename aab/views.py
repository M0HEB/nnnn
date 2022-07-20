from django.shortcuts import render
from django.http import HttpResponse
# from requests import request
# Create your views here.

def home (request):
    return HttpResponse('<h1>my first django app</h1>')