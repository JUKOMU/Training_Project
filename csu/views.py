from django.shortcuts import render, HttpResponse, redirect
from csu import models
from django.template import RequestContext
# Create your views here.


def get(request, s):
    return request.POST.get(s)

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html', {'path': '../static/img/toQC.png'})
    else:
        number = get(request, 'number')
        password = get(request, 'password')

def login_qc(request):
    return render(request, 'login.html', {'path': '../static/img/toPW.png'})
