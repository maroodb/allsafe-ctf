import datetime
from django.db import models

from members.models import Member


class ProjectCategory(models.Model):
    category_name = models.CharField(max_length=30, null=False)
    description = models.CharField(max_length=250, null=False)

    def __str__(self):
        temp = self.category_name.replace(' ', '')
        self.tag = temp
        return self.category_name


class Project(models.Model):
    project_name = models.CharField(max_length=30, null=False)
    project_category = models.ForeignKey(ProjectCategory, null=False)
    project_description = models.CharField(max_length=500, null=False)
    date_start = models.DateField(default=datetime.date.today, verbose_name='Start date')
    date_end = models.DateField(blank=True, verbose_name='Finish date')
    responsables = models.ManyToManyField(Member)
    image = models.ImageField(upload_to='projects/')

    def __str__(self):
        temp = self.project_name.replace(' ', '')
        self.tag = temp
        return self.project_name
