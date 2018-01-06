# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
# 注册模型 即在后台Admin管理中  可以操作数据库中数据
from models import Article
admin.site.register(Article)
