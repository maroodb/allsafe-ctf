from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=1000)

    def __str__(self):
        return self.name


class Visitor(models.Model):
    ip = models.CharField(max_length=200)
    user_agent_id = models.CharField(max_length=200)

    def __str__(self):
        return self.ip
