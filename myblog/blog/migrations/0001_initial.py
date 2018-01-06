# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-01-04 12:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                # id是一个自动字段 因为未添加主键 如果添加主键 id就不会自动生成了
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Title', max_length=32)),
                ('content', models.TextField(null=True)),
            ],
        ),
    ]
