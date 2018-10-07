

import os

import markdown

from django.shortcuts import render,HttpResponse,redirect,reverse,get_object_or_404
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from blog import models
from comments.forms import CommentForm
# Create your views here.

def markdown_convert_html(obj_list):
    """ markdown格式转换成html格式 """

    if type(obj_list) is QuerySet:
        for item in obj_list:
            item.body = markdown.markdown(item.body,
                                          extensions=[
                                              'markdown.extensions.extra',
                                              'markdown.extensions.codehilite',
                                              'markdown.extensions.toc',
                                          ])
        return obj_list

    else:
        obj_list.body = markdown.markdown(obj_list.body,
                                      extensions=[
                                          'markdown.extensions.extra',
                                          'markdown.extensions.codehilite',
                                          'markdown.extensions.toc',
                                      ])
        return obj_list


def index(request):
    """博客首页"""

    # 获取所有的文章对象以降序排列,既最新的文章的最前面
    post_list = models.Post.objects.all()
    # 文章是markdown形式存储在数据库里,所以先markdown格式转换成html格式便于在前端直接渲染成页面
    post_list = markdown_convert_html(post_list)

    return render(request, 'blog/index.html', {'post_list': post_list,})

def article_detail(request,pk):
    """ 文章详情 """

    # 判断传入的文章id是否存在,如果存在就返回查询到的文章对象
    post = get_object_or_404(models.Post,pk=pk)
    # 文章是markdown形式存储在数据库里,所以先markdown格式转换成html格式便于在前端直接渲染成页面
    post = markdown_convert_html(post)
    form = CommentForm()
    comment_list = post.comment_set.all()
    print(comment_list,type(comment_list))
    context = {'post': post,
               'form': form,
               'comment_list': comment_list
               }

    return render(request, 'blog/article_detail.html',context=context)

def archives(request,year,month):
    """ 时间归档查询"""

    # 根据客户端提交的时间关键字,查询这个时间段内的文章
    post_list = models.Post.objects.filter(
        created_time__year=year,
        created_time__month=month,

    )

    # 文章是markdown形式存储在数据库里,所以先markdown格式转换成html格式便于在前端直接渲染成页面
    post_list = markdown_convert_html(post_list)
    return render(request,'blog/index.html',{'post_list':post_list})