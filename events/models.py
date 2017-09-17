from django.db import models

from members.models import Member


class Sponsor(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='sponsors/logos')

    def __str__(self):
        return self.name


class Speaker(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/speaker.png')


class Event(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField(max_length=2000)
    time = models.DateTimeField()
    poster = models.ImageField(upload_to='posters/', default='posters/default.png')
    overview = models.URLField()
    sponsors = models.ManyToManyField(Sponsor)
    speakers = models.ManyToManyField(Speaker)
    took_place = models.BooleanField(default=False)
    is_public = models.BooleanField(default=False)
    publisher = models.ForeignKey(Member, default=1)

    def __str__(self):
        return self.name





