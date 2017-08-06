import datetime

from django.db import models

from members.models import Member


class Article(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    image = models.ImageField(upload_to='articles/')
    content = models.TextField(max_length=7000)
    date = models.DateField(default=datetime.date.today)
    authors = models.ForeignKey(Member)
    is_validated = models.BooleanField(default=False)

    def __str__(self):
        return self.title
