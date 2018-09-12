# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-16 09:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.CharField(max_length=50)),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Competition')),
                ('grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Grade')),
            ],
        ),
        migrations.RemoveField(
            model_name='student',
            name='awardsnum',
        ),
        migrations.RemoveField(
            model_name='student',
            name='competition',
        ),
        migrations.RemoveField(
            model_name='student',
            name='grade',
        ),
    ]