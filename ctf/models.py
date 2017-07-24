from django.db import models
from django.utils import timezone


class CTFtype(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name


class Challenge(models.Model):
    name = models.CharField(max_length=80)
    category = models.ForeignKey(CTFtype)
    description = models.TextField(max_length=500)
    points = models.IntegerField()
    flag = models.CharField(max_length=500)


class ExternalCTF(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField()
    end_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
