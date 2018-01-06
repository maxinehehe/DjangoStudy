# -*- coding:utf-8 -*-
from django.conf.urls import url   # 此句是配置url必需
from  . import views
# urls 是配置路由的地方
urlpatterns = [
    url(r'^index/$', views.index),
    # ^表示开头，$表示结尾 【正则表达式】 ^$表示约束空字符 否则localhost:8000/index/.....都可以访问到此
    # 坑：url(r'^index$', views.index),   正确：url(r'^index/$', views.index),
    url(r'^article/(?P<article_id>[0-9]+)$', views.article_page, name='article_page')
    # (?P<article_id>[0-9]+) 组名
    # name='变量' 传递给
]