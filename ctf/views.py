from django.shortcuts import render

from ctf.models import ExternalCTF
from django.utils import timezone


def scoreboard(request):
    score = "active open selected"
    externals_ctfs = ExternalCTF.objects.filter(end_date__gt=timezone.now())
    return render(request, "ctf/scoreboard.html", locals())


def upload(request):
    return render(request, "ctf/uploadctf.html", locals())
