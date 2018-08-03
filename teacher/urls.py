#-*- coding: UTF-8 -*-
"""定义teacher的url模式"""
from django.conf.urls import url
from django.contrib.auth.views import login
from . import views
urlpatterns = [
    #教师录入界面
    url(r'^tea_entry/$',views.entry,name='tea_entry'),
    #教师查询界面
    url(r'^tea_query/$',views.query,name='tea_query'),
    #教师登录界面
    url(r'^tea_login/$',login,{'template_name':'teacher/tea_login.html'},name='tea_login'),
    #教师注销
    url(r'^tea_logout/$',views.logout_view,name='tea_logout'),
    #教师主页
    url(r'^tea_index/$',views.index,name='tea_index'),
]
