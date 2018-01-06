# -*- coding: utf-8 -*-
from __future__ import unicode_literals

'''
    Django是MVT的模式
    M:  models.py 负责操作数据库相关
    V:  views.py 负责controller的任务 即收到前端数据 -》编写对应操作-》传至前端 起java中Servlet的作用 控制器
    T:  templates 模板 即前端展示 也可以理解为mvc模式中的view 即展示界面
'''


from django.shortcuts import render     # 生成应用时自动添加  render 渲染的意思
from django.http import HttpResponse

from . import models

def index(request):
    # return  HttpResponse('Hello,World!')
    articles = models.Article.objects.all()#.get(pk=1)  # all()查询返回的就是一个列表
    return render(request, 'blog/index.html',{'articles':articles})  # 传到前台  之后注意编写前台代码
    # return render(request,'blog/index.html')   #,{'hello':'Hello,Blog!瞎写的'})
# render(request, 模板文件， 传递到前台的数据)  # 模板

def article_page(request, article_id):  # 在url中奋发又怎么体现呢
    '''
    响应前端函数
    :param request:
    :return:
    '''
    article = models.Article.objects.get(pk=article_id)   # 传什么参数？  前端是点击主页面的超链接进来的
    # 拿到点击文章的唯一标示：主键  修改views.py  参数 来传递关键参数
    # 最后渲染到模板里
    return render(request, 'blog/article_page.html', {'article':article})  # 渲染到模板






