from django.db import models

from members.models import Member
from django.utils import timezone


class Message(models.Model):
    from_user = models.ForeignKey(Member)
    date = models.DateTimeField(default=timezone.now)
    content = models.TextField(max_length=5000)
    seen = models.BooleanField(default=False)


class Inbox(models.Model):
    owner = models.OneToOneField(Member)
    messages = models.ManyToManyField(Message)


class Broadcast(models.Model):
    title = models.CharField(max_length=150)


class Activity(models.Model):
    title = models.CharField(max_length=120)
    date = models.DateTimeField(default=timezone.now)
    description = models.TextField(max_length=4000)
    publisher = models.ForeignKey(Member)

    def __str__(self):
        return self.title


