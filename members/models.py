import datetime
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Position(models.Model):
    position = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.position


class Member(models.Model):
    man = 'M'
    woman = 'Ms'
    genderChoice = (
        (man, 'Man'),
        (woman, 'Woman'),)

    gender = models.CharField(
        max_length=2,
        choices=genderChoice,
        default=man,
    )

    user = models.OneToOneField(User)

    avatar = models.ImageField(default="avatars/default.png", null=True, blank=True, upload_to="avatars/")
    birthday = models.DateField(null=True, default=datetime.date.today)
    function = models.ForeignKey(Position, null=True)
    status = models.CharField(max_length=80, default="#")
    linkedin = models.CharField(default='#', max_length=300, blank=True)
    facebook = models.CharField(default='#', max_length=300, blank=True)
    score = models.IntegerField(default=0)
    phone = models.IntegerField(default=1111)
    date_of_join = models.DateTimeField(default=timezone.now)
    last_resolved_ctf = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "{0}".format(self.user)


class Task(models.Model):
    tsk_title = models.CharField(max_length=30)
    tsk_description = models.TextField(max_length=400)
    tsk_responsables = models.ManyToManyField(Member)
    tsk_start_date = models.DateTimeField(default=timezone.now)
    tsk_done_date = models.DateTimeField(default=timezone.now, null=True)
    tsk_deadline = models.DateTimeField(default=timezone.now, null=True)
    tsk_is_in_progress = models.BooleanField(default=False)
    tsk_is_done = models.BooleanField(default=False)
    tsk_is_out_date = models.BooleanField(default=False)

    def __str__(self):
        return self.tsk_title

    def isoutdate(self):
        nowtime = timezone.now()
        if nowtime > self.tsk_deadline and not self.tsk_is_done:
            self.tsk_is_in_progress = False
            self.tsk_is_done = False
            self.tsk_is_out_date = True
            return True
        else:
            return False


class FakeUser(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=80)

    def __str__(self):
        return self.email


