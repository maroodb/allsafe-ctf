import datetime

from django.db import models


class Slide(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    background = models.ImageField(upload_to='slides/')
    link = models.CharField(default='#', max_length=800)
    date = models.DateField(default=datetime.date.today)
    text_over_link = models.CharField(max_length=50, default='View More')
    there_is_link = models.BooleanField(default=False)

    def __str__(self):
        return self.title
