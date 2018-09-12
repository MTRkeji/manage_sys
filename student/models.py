#-*- coding: UTF-8 -*-
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#年级
class Sclass(models.Model):
    #年级名字
    name = models.CharField(max_length = 30,verbose_name="年级")
    def __str__(self):
        return self.name
#获奖等级
class Grade(models.Model):
    #等级名称
    name = models.CharField(max_length = 50,verbose_name="获奖等级")
    def __str__(self):
        return self.name
#竞赛
class Competition(models.Model):
    #竞赛名称
    name = models.CharField(max_length = 100,verbose_name="竞赛名称")
    #主办方
    sponser = models.CharField(max_length = 100,verbose_name="主办方")
    #开始时间
    startdate = models.DateField(auto_now_add=True,verbose_name="创办时间")
    def __str__(self):
        return self.name
#学生
class Student(models.Model):
    #学生账户
    user = models.OneToOneField(User,on_delete=models.CASCADE,verbose_name="学号")
    #姓名
    name = models.CharField(max_length = 50,verbose_name="姓名")
    #年级
    sclass = models.ForeignKey(Sclass,on_delete=models.CASCADE,verbose_name="年级")
    def __str__(self):
        return self.name
#记录
class Entry(models.Model):
    xuehao = models.CharField(max_length = 12,verbose_name='学号')
    student = models.CharField(max_length = 50,verbose_name="学生姓名")
    competition = models.ForeignKey(Competition,on_delete=models.CASCADE,verbose_name="竞赛名称")
    grade = models.ForeignKey(Grade,on_delete=models.CASCADE,verbose_name="获奖情况")
    attachment = models.CharField(max_length = 200,null=True,blank=True)
    shenhe = models.BooleanField(default = False)
    def __str__(self):
        return self.student
    

