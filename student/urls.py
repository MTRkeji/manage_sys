#-*- coding: UTF-8 -*-
"""定义student的url模式"""
from django.conf.urls import url
from django.contrib.auth.views import login
from . import views
urlpatterns = [
    #学生获奖信息录入界面
    url(r'^stu_entry/$',views.entry,name='stu_entry'),
    #学生获奖信息查看界面
    url(r'^stu_info/$',views.info,name='stu_info'),
    #学生登录界面
    url(r'^stu_login/$',login,{'template_name':'student/stu_login.html'},name='stu_login'),
    #学生注销
    url(r'^stu_logout/$',views.logout_view,name='stu_logout'),
    #学生主界面
    url(r'^stu_index/$',views.index,name='stu_index'),
]
