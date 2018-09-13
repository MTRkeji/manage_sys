# -*- coding: UTF-8 -*-
"""teacher的视图"""
from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from student import forms, models
import os
from django.conf import settings
from xlwt import *
from io import BytesIO


# Create your views here.
# 教师录入信息视图函数
@login_required
def entry(request):
    name = request.user.username
    if request.method != 'POST':
        competitions = models.Competition.objects.all()
        grades = models.Grade.objects.all()
    else:
        new_entry = models.Entry()
        new_entry.xuehao = request.POST['xuehao']
        user = auth.models.User.objects.get(username=request.POST['xuehao'])
        new_entry.student = models.Student.objects.get(user=user).name
        new_entry.competition = models.Competition.objects.get(name=request.POST.get('competition'))
        new_entry.grade = models.Grade.objects.get(name=request.POST.get('grade'))
        attachment = request.FILES.get('attachment')
        if attachment:
            mypath = os.path.join(settings.MEDIA_ROOT, new_entry.xuehao)
            isExists = os.path.exists(mypath)
            if not isExists:
                os.makedirs(mypath)
            f = open(os.path.join(mypath, attachment.name), 'wb+')
            for line in attachment.chunks():
                f.write(line)
            f.close()
            new_entry.attachment = os.path.join(new_entry.xuehao, attachment.name)
        else:
            new_entry.attachment = None
        new_entry.shenhe = True
        new_entry.save()
        msg = "添加成功！"
        competitions = models.Competition.objects.all()
        grades = models.Grade.objects.all()
        context = {'name': name, 'competitions': competitions, 'grades': grades, 'msg': msg}
        return render(request, 'teacher/tea_entry.html', context)
    context = {'name': name, 'competitions': competitions, 'grades': grades}
    return render(request, 'teacher/tea_entry.html', context)


# 教师查询视图函数
@login_required
def query_xuehao(request):
    msg = ""
    name = request.user.username
    if request.method == 'POST':
        if 'select' in request.POST:
            user = auth.models.User.objects.get(username=request.POST['xuehao'])
            if user:
                studentname = models.Student.objects.get(user=user).name
                entrys = models.Entry.objects.filter(student=studentname, shenhe=True)
                context = {'entrys': entrys, 'name': name}
                return render(request, 'teacher/tea_query_xuehao.html', context)
        elif 'delete' in request.POST:
            idlist = request.POST.getlist('ids')
            idstring = ','.join(idlist)
            models.Entry.objects.extra(where=['id IN (' + idstring + ')']).delete()
            msg = "删除操作成功！"
    context = {'name': name, 'msg': msg}
    return render(request, 'teacher/tea_query_xuehao.html', context)


@login_required
def query_competition(request):
    name = request.user.username
    competition = ''
    msg = ""
    entrys = None
    if request.method == 'POST':
        if 'select' in request.POST:
            competition = models.Competition.objects.get(name=request.POST['competition'])
            if competition:
                entrys = models.Entry.objects.filter(competition=competition, shenhe=True)
                context = {'entrys': entrys, 'name': name, 'competition': competition}
                return render(request, 'teacher/tea_query_competition.html', context)
        elif 'delete' in request.POST:
            competition = models.Competition.objects.get(name=request.POST['competition'])
            idlist = request.POST.getlist('ids')
            idstring = ','.join(idlist)
            models.Entry.objects.extra(where=['id IN (' + idstring + ')']).delete()
            entrys = models.Entry.objects.filter(competition=competition, shenhe=True)
            msg = "删除操作成功！"
        elif 'export' in request.POST:
            competition = models.Competition.objects.get(name=request.POST['competition'])
            entrys = models.Entry.objects.filter(competition=competition, shenhe=True)
            if entrys:
                ws = Workbook(encoding="utf-8")
                w = ws.add_sheet(u'数据报表第一页')
                w.write(0, 0, u'学号')
                w.write(0, 1, u'姓名')
                w.write(0, 2, u'竞赛')
                w.write(0, 3, u'奖项')
                excel_row = 1
                for entry in entrys:
                    w.write(excel_row, 0, entry.xuehao)
                    w.write(excel_row, 1, entry.student)
                    w.write(excel_row, 2, entry.competition.name)
                    w.write(excel_row, 3, entry.grade.name)
                    excel_row += 1
                sio = BytesIO()
                ws.save(sio)
                sio.seek(0)
                response = HttpResponse(sio.getvalue(), content_type='application/vnd.ms-excel')
                response['Content-Disposition'] = 'attachment;filename=report.xlsx'
                response.write(sio.getvalue())
                return response
    context = {'name': name, 'msg': msg, 'competition': competition, 'entrys': entrys}
    return render(request, 'teacher/tea_query_competition.html', context)


# 教师审核视图
@login_required
def check(request):
    name = request.user.username
    msg = ""
    if request.method == 'POST':
        if 'select' in request.POST:
            competition = models.Competition.objects.get(name=request.POST['competition'])
            if competition:
                entrys = models.Entry.objects.filter(competition=competition, shenhe=False)
                context = {'entrys': entrys, 'name': name}
                return render(request, 'teacher/tea_check.html', context)
        elif 'check' in request.POST:
            idlist = request.POST.getlist('ids')
            idstring = ','.join(idlist)
            models.Entry.objects.extra(where=['id IN (' + idstring + ')']).update(shenhe=True)
            msg = "审核操作成功！"
        elif 'delete' in request.POST:
            idlist = request.POST.getlist('ids')
            idstring = ','.join(idlist)
            models.Entry.objects.extra(where=['id IN (' + idstring + ')']).delete()
            msg = "删除操作成功！"
    context = {'name': name, "msg": msg}
    return render(request, 'teacher/tea_check.html', context)


# 教师注销视图
@login_required
def logout_view(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse("teacher:tea_index"))


# 教师主页视图
def index(request):
    cap_form = forms.LoginForm()
    msg = ''
    if request.user.is_authenticated:
        username = request.user.username
        context = {'name': username}
        return render(request, 'teacher/tea_index.html', context)
    context = {'cap_form': cap_form}
    return render(request, 'teacher/tea_login.html', context)


# 登录视图
def login_view(request):
    if request.method == 'POST':
        cap_form = forms.LoginForm(request.POST)
        if cap_form.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse("teacher:tea_index"))
            else:
                msg = '帐号或密码错误！'
        else:
            msg = '验证码错误！'
    else:
        cap_form = forms.LoginForm()
        msg = ''
    context = {'cap_form': cap_form, 'msg': msg}
    return render(request, 'teacher/tea_login.html', context)