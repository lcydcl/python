#!/usr/bin/env python
#coding:utf-8
from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from app01 import models
from django.contrib import auth
# Create your views here.

def login(request):
    if request.method=='POST':
        username,password=request.POST.get('username'),request.POST.get('password')
        re=auth.authenticate(username=username,password=password)
        if re is not None: 
            auth.login(request,re)
            return redirect('/index/')
        else:
            return render_to_response('login.html',{'login_error':'用户名或密码错误'})
                
    return render_to_response('login.html')
def logout(request):
    pass
def index(request):
    rooms=models.ChatRoom.objects.all()
    return render_to_response('index.html',{'rooms':rooms})
    
def room(request):
    pass

    
