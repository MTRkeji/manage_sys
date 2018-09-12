#-*- coding: UTF-8 -*-
from django import forms
from captcha.fields import CaptchaField
from . import models

class LoginForm(forms.Form):
    captcha = CaptchaField(error_messages={'invalid':u'验证码错误!'})
