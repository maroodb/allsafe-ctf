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

