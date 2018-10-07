
from django import template
from blog import models

# 实例化一个模板类
register = template.Library()


@register.simple_tag
def get_recent_posts(num=5):
    """最新文章展示"""
    return models.Post.objects.all().order_by('-created_time')[:num]

@register.simple_tag
def archives():
    """按时间归档"""
    # created_time是创建时间 month是时间精度到月份 DESC降序
    return models.Post.objects.dates('created_time','month',order='DESC')

@register.simple_tag
def get_categories():
    """按分类归档"""
    return models.Category.objects.all()