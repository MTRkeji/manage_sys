#-*- coding: UTF-8 -*-
"""定义teacher的url模式"""
from django.conf.urls import url
from django.contrib.auth.views import login
from . import views
urlpatterns = [
    #教师录入界面
    url(r'^tea_entry/$',views.entry,name='tea_entry'),
    #教师查询界面
    url(r'^tea_query_xuehao/$',views.query_xuehao,name='tea_query_xuehao'),
    url(r'^tea_query_competition/$',views.query_competition,name='tea_query_competition'),
    #教师审核界面
    url(r'^tea_check/$',views.check,name='tea_check'),
    #教师登录界面
    url(r'^tea_login/$',views.login_view,name='tea_login'),
    #教师注销
    url(r'^tea_logout/$',views.logout_view,name='tea_logout'),
    #教师主页
    url(r'^tea_index/$',views.index,name='tea_index'),
]
