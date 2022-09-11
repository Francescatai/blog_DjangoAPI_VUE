from django.db import models
import random


# Create your models here.


# 默認個人簡介
def default_sign():
    signs = ['歡迎來到個人blog', '歡迎多多交流']
    return random.choice(signs)


class UserProfile(models.Model):
    username = models.CharField(max_length=10, verbose_name='用戶名', primary_key=True)
    nickname = models.CharField(max_length=10, verbose_name='暱稱')
    password = models.CharField(max_length=8)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    avatar = models.ImageField(upload_to='avatar', null=True)
    sign = models.CharField(max_length=50, verbose_name='個人簡介', default=default_sign)
    info = models.CharField(max_length=200, verbose_name='詳細資訊', default='')
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    # table name
    class Meta:
        db_table = 'user_user_profile'
