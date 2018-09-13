from django.contrib import admin
from . import models
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user','name','sclass')
class CompetitionAdmin(admin.ModelAdmin):
    list_display = ('name','sponser','startdate')
class EntryAdmin(admin.ModelAdmin):
    list_display = ('student','competition','grade')
admin.site.register(models.Sclass)
admin.site.register(models.Student,StudentAdmin)
admin.site.register(models.Grade)
admin.site.register(models.Competition,CompetitionAdmin)
admin.site.register(models.Entry,EntryAdmin)