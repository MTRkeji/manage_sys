#-*- coding: UTF-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.
#学生录入视图
@login_required
def entry(request):
    return render(request,'student/stu_entry.html')

#学生信息视图
@login_required
def info(request):
    return render(request,'student/stu_info.html')

#学生注销视图
@login_required
def logout_view(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse("student:stu_index"))
#学生主页视图
def index(request):
    if request.user.is_authenticated():
        username = request.user.username
        context = {'username':username}
        return render(request,'student/stu_index.html',context)
    return render(request,'student/stu_index.html')
