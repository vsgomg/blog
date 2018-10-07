from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    """ 文章分类 """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    '''标签'''

    name = models.CharField(max_length=100)

class Post(models.Model):
    '''文章'''
    title = models.CharField(max_length=70)
    # 文章内容
    body = models.TextField()
    # 创建时间
    created_time = models.DateTimeField()
    # 修改时间
    modified_time = models.DateTimeField()
    # 文章摘要
    excerpt = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag,blank=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('blog:article_detail',kwargs={'pk':self.pk})
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_time']