import datetime

import requests
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from accounts.forms import ConnexionForm, RegistrationForm, MemberForm
from ctf.models import ExternalCTF
from home.views import home
from members.models import FakeUser
from django.utils import timezone


@login_required
def dashboard(request):

    user = request.user
    externals_ctfs = ExternalCTF.objects.filter(end_date__gt=timezone.now())
    return render(request, 'accounts/home.html', locals())


def login_view(request):
    error = False
    sql = False
    if request.user.is_authenticated():
        return redirect(dashboard)

    if request.method == "POST":

        form = ConnexionForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]

            password = form.cleaned_data["password"]

            user = authenticate(username=username, password=password)

            if user:  # Si l'objet renvoyé n'est pas None

                login(request, user)  # nous connectons l'utilisateur
                return redirect(dashboard)

            if '=' in username and 'or' in username or ('=' in password and 'or' in password):
                sql = True
            else:

                error = True

    else:

        form = ConnexionForm()

    return render(request, 'accounts/login.html', locals())


def logout(request):
    logout(request)
    return redirect(home)


@login_required
def my_profile(request):

    profile="active"
    today = datetime.date.today().strftime('%Y-%m-%d')
    current_user = request.user
    member = current_user.member
    if request.method == "POST":

        slogan=request.POST.get('slogan', None)
        date_birth=request.POST.get('date', None)
        gender=request.POST.get('gender')
        linkedin=request.POST.get('linkedin', None)
        facebook=request.POST.get('facebook', None)
        birthday = datetime.datetime.strptime(date_birth, '%Y-%m-%d').date()

        member.status = slogan
        member.linkedin = linkedin
        member.facebook = facebook
        member.gender = gender
        member.birthday = birthday

        member.save()

    return render(request, 'accounts/dashboard.html', locals())


def signup(request):
    user_form = RegistrationForm(request.POST or None)
    if request.method == "POST":
        post = True
        valcaptcha = request.POST.get("g-recaptcha-response")

        url = 'https://www.google.com/recaptcha/api/siteverify'
        data = {
            'secret': '6LcxfiEUAAAAANAbaIof6VfqxYLDWvGdvPEIkC_M',
            'response': valcaptcha,
        }

        r = requests.post(url, data)
        result = r.json()
        success = result["success"]
        if success:
            if user_form.is_valid():
                username = user_form.cleaned_data["username"]
                password = user_form.cleaned_data["password1"]
                first_name = user_form.cleaned_data["first_name"]
                last_name = user_form.cleaned_data["last_name"]
                email = user_form.cleaned_data["email"]

                fake_user = FakeUser()
                fake_user.email = email
                fake_user.password = password

                user = User.objects.create_user(username, email, password)
                user.is_active = False
                user.first_name = first_name
                user.last_name = last_name

                user.save()
                fake_user.save()
                received = True
            else:
                received = False

    return render(request, "accounts/signup.html", locals())