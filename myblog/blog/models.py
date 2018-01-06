# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# 操作数据库相关models
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=32, default='Title' )  # max_length=必须有
    content =  models.TextField(null=True)  # 允许为空
    def __unicode__(self):
        return self.title  # 使后台显示标题