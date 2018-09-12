from django.db import models

# Create your models here.
class MyMessage(models.Model):
    title = models.CharField(max_length=100,verbose_name='标题')
    content = models.TextField(verbose_name='内容')
    upload_time = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class TeaMessage(models.Model):
    title = models.CharField(max_length=100, verbose_name='标题')
    content = models.TextField(verbose_name='内容')
    upload_time = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
class StuMessage(models.Model):
    title = models.CharField(max_length=100, verbose_name='标题')
    content = models.TextField(verbose_name='内容')
    upload_time = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title