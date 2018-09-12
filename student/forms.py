#-*- coding: UTF-8 -*-
from django import forms
from captcha.fields import CaptchaField
from . import models
class EntryForm(forms.ModelForm):
    class Meta:
        model = models.Entry
        fields = ['competition','grade']
        labels = {'competition':'','grade':''}
class LoginForm(forms.Form):
    captcha = CaptchaField(error_messages={'invalid':u'验证码错误!'})
