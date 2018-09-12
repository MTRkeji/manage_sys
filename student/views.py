#-*- coding: UTF-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from . import models
from . import forms
import os
from django.conf import settings
# Create your views here.
#学生录入视图
@login_required
def entry(request):
    user = request.user
    xuehao = user.username
    student = models.Student.objects.get(user=user)
    name = student.name
    if request.method != 'POST':
        competitions = models.Competition.objects.all()
        grades = models.Grade.objects.all()
    else:
        new_entry = models.Entry()
        new_entry.xuehao = xuehao
        new_entry.student = name
        new_entry.competition = models.Competition.objects.get(name=request.POST.get('competition'))
        new_entry.grade = models.Grade.objects.get(name=request.POST.get('grade'))
        attachment = request.FILES.get('attachment')
        if attachment:
            mypath = os.path.join(settings.MEDIA_ROOT,xuehao)
            isExists = os.path.exists(mypath)
            if not isExists:
                os.makedirs(mypath)
            f = open(os.path.join(mypath,attachment.name),'wb+')
            for line in attachment.chunks():
                f.write(line)
            f.close()
            new_entry.attachment = os.path.join(xuehao,attachment.name)
        else:
            new_entry.attachment = None
        new_entry.shenhe = False
        new_entry.save()
        msg = "添加成功！正在审核中..."
        competitions = models.Competition.objects.all()
        grades = models.Grade.objects.all()
        context = {'xuehao':xuehao,'name':name,'competitions':competitions,'grades':grades,'msg':msg}
        return render(request,'student/stu_entry.html',context)
    context = {'xuehao':xuehao,'name':name,'competitions':competitions,'grades':grades}
    return render(request,'student/stu_entry.html',context)

#学生信息视图
@login_required
def info(request):
    xuehao = request.user.username
    student = models.Student.objects.get(user = request.user)
    name = student.name
    entrys = models.Entry.objects.filter(xuehao=xuehao)
    context = {'xuehao':xuehao,'entrys':entrys,'name':name}
    return render(request,'student/stu_info.html',context)

#学生注销视图
@login_required
def logout_view(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse("student:stu_index"))
#学生主页视图
def index(request):
    cap_form = forms.LoginForm()
    msg = ''
    if request.user.is_authenticated():
        student = models.Student.objects.get(user=request.user)
        username = student.name
        context = {'name':username}
        return render(request,'student/stu_index.html',context)
    context = {'cap_form':cap_form}
    return render(request,'student/stu_login.html',context)

#学生登录视图
def login_view(request):
    if request.method == 'POST':
        cap_form = forms.LoginForm(request.POST)
        if cap_form.is_valid():            
            username = request.POST.get('username','')
            password = request.POST.get('password','')
            user = auth.authenticate(username=username,password=password)
            if user is not None and user.is_active:
                auth.login(request,user)
                return HttpResponseRedirect(reverse("student:stu_index"))
            else:
                msg = '帐号或密码错误！'
        else:
            msg = '验证码错误！'
    else:
        cap_form = forms.LoginForm()
        msg = ''
    context = {'cap_form':cap_form,'msg':msg}
    return render(request,'student/stu_login.html',context)
