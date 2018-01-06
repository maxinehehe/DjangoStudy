# -*- coding: utf-8 -*-
# from __future__ import unicode_literals  # 必须出现在文件的开头

from django.shortcuts import render     # 生成应用时自动添加  render 渲染的意思
from django.http import HttpResponse

def index(request):
    # return  HttpResponse('Hello,World!')
    return render(request,'blog2/index.html')   #,{'hello':'Hello,Blog!瞎写的'})
# render(request, 模板文件， 传递到前台的数据)  # 模板
# Create your views here.

# Create your views here.
