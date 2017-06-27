import datetime

from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from accounts.forms import ConnexionForm
from home.views import home


@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html')


def login(request):
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

