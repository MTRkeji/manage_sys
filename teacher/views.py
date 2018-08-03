#-*- coding: UTF-8 -*-
"""teacher的视图"""
from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.
#教师录入信息视图函数
@login_required
def entry(request):
    return render(request,'teacher/tea_entry.html')

#教师查询视图函数
@login_required
def query(request):
    return render(request,'teacher/tea_query.html')

#教师注销视图
@login_required
def logout_view(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse("teacher:tea_index"))
    
#教师主页视图
def index(request):
    if request.user.is_authenticated():
        username = request.user.username
        context = {'username':username}
        return render(request,'teacher/tea_index.html',context)
    return render(request,'teacher/tea_index.html')
