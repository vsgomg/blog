from django.test import TestCase

# Create your tests here.
import os
import django
import markdown
from django.utils import timezone
import datetime


if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myblog.settings")
    django.setup()

    from blog import models

    post_list = models.Post.objects.filter(created_time__year=2018,
                                           created_time__month=10,

                                    ).order_by('-created_time')
    print(111, post_list)
    print(timezone.now())
    print(datetime.datetime.now())
