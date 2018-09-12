from django.contrib import admin
from .models import MyMessage,TeaMessage,StuMessage
# Register your models here.
admin.site.register(MyMessage)
admin.site.register(TeaMessage)
admin.site.register(StuMessage)