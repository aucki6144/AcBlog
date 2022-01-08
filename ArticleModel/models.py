from django.db import models


# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=30)
    time = models.DateField(auto_now_add=True)
    about = models.TextField(default="Empty")
    text = models.TextField(default="Empty")
    watch_num = models.IntegerField(default=0)
    comment_num = models.IntegerField(default=0)
    img_src = models.URLField(max_length=100)

    def getTitle(self):
        return self.title

    def getTime(self):
        return self.time

    def getAbout(self):
        return self.about

    def getText(self):
        return self.text

