# Generated by Django 4.1.1 on 2022-09-10 14:23

from django.db import migrations, models
import user.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('username', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='用戶名')),
                ('nickname', models.CharField(max_length=10, verbose_name='暱稱')),
                ('password', models.CharField(max_length=8)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=10)),
                ('avatar', models.ImageField(null=True, upload_to='avatar')),
                ('sign', models.CharField(default=user.models.default_sign, max_length=50, verbose_name='個人簡介')),
                ('info', models.CharField(default='', max_length=200, verbose_name='詳細資訊')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'user_user_profile',
            },
        ),
    ]
