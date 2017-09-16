from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect

from ctf.forms import UploadForm
from ctf.models import ExternalCTF, CTFtype, Challenge
from django.utils import timezone
import hashlib

from members.models import Member


@login_required
def scoreboard(request):
    score = "active"
    externals_ctfs = ExternalCTF.objects.filter(end_date__gt=timezone.now())

    top_members = Member.objects.filter(user__is_active=True).order_by('-score', '-time_of_last_hack')
    return render(request, "ctf/scoreboard.html", locals())


@login_required
def upload(request):
    upld = "active"
    categories = CTFtype.objects.all()
    upload_form = UploadForm(request.POST or None, request.FILES)
    if request.method == "POST" and request.FILES:
        posted = True
        if upload_form.is_valid():
            valide = True
            file = upload_form.cleaned_data["file"]
            name = upload_form.cleaned_data["name"]
            category = upload_form.cleaned_data["category"]
            flag = upload_form.cleaned_data["flag"]
            points = upload_form.cleaned_data["points"]
            description = upload_form.cleaned_data["description"]

            hashed_flag = hashlib.sha1(flag.encode()).hexdigest()

            challenge = Challenge()
            challenge.uploader = request.user.member
            challenge.name = name
            challenge.category = CTFtype.objects.get(name=category)
            challenge.description = description
            challenge.points = points
            challenge.flag = hashed_flag
            challenge.file = file
            challenge.save()
            done = True

    return render(request, "ctf/uploadctf.html", locals())


@login_required
def challenges(request):
    # online_users = User.objects.filter()
    challenge = "active"
    active_member = request.user.member
    ctf_types = CTFtype.objects.all()
    ctfs = Challenge.objects.exclude(Q(uploader=active_member) | Q(resolvers=active_member))
    return render(request, "ctf/challenges.html", locals())


@login_required
def ctf_resolve(request, id_ch):
    success = False

    try:
        challenge = Challenge.objects.get(pk=id_ch)
        flag = request.POST.get('flag', "&")
        hashed_flag = hashlib.sha1(flag.encode()).hexdigest()

        if hashed_flag == challenge.flag:
            pts = challenge.points + request.user.member.score
            request.user.member.score = pts
            request.user.member.date_of_last_hack = timezone.now()
            request.user.member.save()
            challenge.resolvers.add(request.user.member)
            success = True
        else:
            success = False

        return render(request, "ctf/result.html", locals())
    except Challenge.DoesNotExist:
        return redirect('/ctf/challenges')


@login_required
def challenge_details(request, id_ch):
    response = dict()
    try:

        challenge = Challenge.objects.get(pk=id_ch)
        response["success"] = True
        response["name"] = challenge.name
        response["author"] = challenge.uploader.user.username
        response["description"] = challenge.description
        response["points"] = challenge.points
        response["date"] = challenge.date.strftime("%d %B %Y %H:%M:%S")
        response["resolvers"] = challenge.resolvers.count()
        response["category"] = challenge.category.name

    except Challenge.DoesNotExist:
        response["success"] = False

    return JsonResponse(response)
