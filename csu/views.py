from django.shortcuts import render, HttpResponse, redirect
from csu import models
from django.template import RequestContext
# Create your views here.

def get(request, s):
    return request.POST.get(s)
def login(request):
    return render(request, 'login.html')