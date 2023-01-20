from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from csu import models
from django.template import RequestContext
# Create your views here.

def get(request, s):
    return request.POST.get(s)

def register(request):
    if request.method == "GET":
        # get请求直接返回页面
        return render(request, "register.html")
    if request.method == "POST":
        # 获取post请求数据
        u = get(request, 'username')
        p1 = get(request, 'password')
        # 查询数据库
        data_list = models.User.objects.all()
        for obj in data_list:
            if u == obj.name:
                return render(request, "register.html", {"n1": "该用户名已被注册!"})
        """
        无查询结果，注册该用户，并返回提示登录信息
        """
        models.User.objects.create(number=u, password=p1)
        return render(request, "register.html", {"n1": "注册成功!"})

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html', {'path': '../static/img/toQC.png'})
    else:
        username = get(request, 'username')
        password = get(request, 'password')
        if username == 'admin' and password == '123':
            return render(request, 'index.html')
        data_list = models.User.objects.all()
        for obj in data_list:
            if username == obj.number:
                if password == obj.password:
                    return HttpResponseRedirect('/index/?message=pass'+username)
        return render(request, "login.html", {"n": "您提供的用户名或者密码有误"})


def login_qc(request):
    return render(request, 'login_qc.html', {'path': '../static/img/toPW.png'})

def login_dc(request):
    return render(request, 'login_dc.html')

def index(request):
    st = request.GET.get('message')
    if st[0:4] == 'pass':
        return render(request, 'index.html', {'username': st[4:]})
    return render(request, 'login.html')