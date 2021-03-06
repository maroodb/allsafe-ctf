import datetime

from django.db import models

from members.models import Member


class News(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    image = models.ImageField(upload_to='news/')
    content = models.TextField(max_length=7000)
    date = models.DateField(default=datetime.date.today)
    publisher = models.ForeignKey(Member, default=1)

    def __str__(self):
        return self.title


class Award(models.Model):
    title = models.CharField(max_length=120)
    position = models.CharField(max_length=100)
    description = models.TextField(max_length=2000)
    image = models.ImageField(upload_to='awards/')

    def __str__(self):
        return self.title

