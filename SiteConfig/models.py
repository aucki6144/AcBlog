from django.db import models

# Create your models here.


class HeaderNotice(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    is_show = models.IntegerField(default=0)
    content = models.TextField(default="请添加文字")


class AboutSite(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    content = models.TextField(default="请填入HTML格式文字")


class Contact(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    imageSrc = models.TextField(default="https://inews.gtimg.com/newsapp_ls/0/14401632748/0.jpg")
    title = models.CharField(max_length=30)
    linkSrc = models.TextField(default="https://www.jinlog.com")


class FriendUrl(models.Model):
    imageSrc = models.TextField(default="https://inews.gtimg.com/newsapp_ls/0/14401632748/0.jpg")
    title = models.CharField(max_length=30)
    subtitle = models.CharField(max_length=50)
    url = models.TextField(default="www.baidu.com")
