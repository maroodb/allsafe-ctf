from django.db import models
from django.utils import timezone

from members.models import Member


class DocumentCategroie(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.name


class Document(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField(max_length=500)
    uploader = models.ForeignKey(Member, default=1)
    tags = models.ManyToManyField(DocumentCategroie, blank=True)
    upload_date = models.DateTimeField(default=timezone.now)
    cover_pic = models.ImageField(upload_to='library/covers/', default='library/covers/default.png', blank=True)
    document_file = models.FileField(upload_to='library/documents/')

    def __str__(self):
        return self.title


