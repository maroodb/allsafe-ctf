from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator
from members.models import Member


class CTFtype(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name


class Challenge(models.Model):
    name = models.CharField(max_length=80)
    category = models.ForeignKey(CTFtype)
    description = models.CharField(max_length=500)
    points = models.PositiveIntegerField(validators=[MinValueValidator(5)])
    file = models.FileField(upload_to='ctf/challenges/', default='ctf/challenges/error.txt')
    flag = models.CharField(max_length=500)
    date = models.DateTimeField(default=timezone.now)
    #hidden = models.BooleanField(default=False)
    uploader = models.ForeignKey(Member, related_name='%(class)s_uploader', default=1)
    resolvers = models.ManyToManyField(Member, related_name='%(class)s_resolvers')

    def __str__(self):
        return self.name


class ExternalCTF(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField()
    end_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


