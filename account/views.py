from django.shortcuts import render
from store.urls import *


# Create your views here.
def acc(request):
    return render(request, 'register.html')


def log(request):
    return render(request, 'login.html')
