from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def register_view(request):
    return HttpResponse("register_view")

def login_view(request):
    return HttpResponse("login_view")

def home_view(request):
    return HttpResponse("home_view")

def show_off_view(request):
    return HttpResponse("show_off_view")
