import datetime

import requests
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect

from accounts.forms import ConnexionForm, RegistrationForm, MemberForm, ImageForm, NewsForm, DocumentForm
from blog.models import News
from ctf.models import ExternalCTF
from events.models import Event
from home.models import Visitor
from home.views import home
from library.models import DocumentCategroie, Document
from members.models import FakeUser, Member, Position
from django.utils import timezone

from messenger.models import Activity


@staff_member_required
def administration(request):

    active_users = User.objects.filter(is_active=True)
    inactive_users = User.objects.filter(is_active=False)
    return render(request, "accounts/admin.html", locals())


@staff_member_required
def account_management(request):

    if request.POST:
        users_list = request.POST.getlist('inactive-users')
        for u in users_list:
            try:
                new_user = User.objects.get(pk=u)
                if not new_user.is_active:
                    new_user.is_active = True
                    new_user.save()
                    html_content = generate_email(new_user.first_name, new_user.username)
                    subject, from_email, to = '[Activation] AllSafe Account', 'contact@allsafeclub.info', new_user.email
                    msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
                    msg.attach_alternative(html_content, "text/html")
                    msg.send()
            except User.DoesNotExist:
                pass

    return redirect('/accounts/admin')


@login_required
def dashboard(request):
    member = request.user.member
    uploads = member.news_set.count() + member.article_set.count() + member.challenge_uploader.count()
    members_count = Member.objects.count()
    web_visitors = Visitor.objects.count()
    externals_ctfs = ExternalCTF.objects.filter(end_date__gt=timezone.now())
    activities = Activity.objects.all().order_by('date')
    events = Event.objects.all().order_by('time')
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


def deconnect(request):
    logout(request)
    return redirect(home)


@login_required
def my_profile(request):
    image_form = ImageForm(request.POST or None, request.FILES)
    profile = "active"
    today = datetime.date.today().strftime('%Y-%m-%d')
    current_user = request.user
    member = current_user.member
    uploads = member.news_set.count() + member.article_set.count() + member.challenge_uploader.count()
    if request.POST and request.FILES:
        if image_form.is_valid():
            image = image_form.cleaned_data["image"]
            member.avatar = image
            member.save()

    elif request.method == "POST":

        testimonial = request.POST.get('testimonial', "")
        date_birth = request.POST.get('birthday', "")
        linkedin = request.POST.get('linkedin', "")
        facebook = request.POST.get('facebook', "")
        phone = request.POST.get("phone", "")
        username = request.POST.get("username", "None")
        if date_birth != "":
            birthday = datetime.datetime.strptime(date_birth, '%Y-%m-%d').date()
            member.birthday = birthday
        if testimonial != "":
            member.status = testimonial
        if linkedin != "":
            member.linkedin = linkedin
        if facebook != "":
            member.facebook = facebook
        if phone != "":
            member.phone = phone
        if username != "":
            request.user.username = username
            request.user.save()
        member.save()

    return render(request, 'accounts/profile.html', locals())


def signup(request):
    user_form = RegistrationForm(request.POST or None)
    if request.method == "POST":
        post = True
        valcaptcha = request.POST.get("g-recaptcha-response")

        url = 'https://www.google.com/recaptcha/api/siteverify'
        data = {
            'secret': '6LdCnhUUAAAAACehzbK9SI9maF9Yfs9KsLfRlytN',
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
                member = Member()
                fake_user.email = email
                fake_user.password = password

                user = User.objects.create_user(username, email, password)
                user.is_active = False
                user.first_name = first_name
                user.last_name = last_name
                member.user = user
                try:
                    default_position = Position.objects.get(position="Member")
                    member.function = default_position
                except Position.DoesNotExist:
                    pass

                user.save()
                member.save()
                fake_user.save()
                received = True
            else:
                received = False

    return render(request, "accounts/signup.html", locals())


@login_required
def inbox(request):
    return render(request, "accounts/inbox.html", locals())


@login_required
def chatroom(request):
    return render(request, "accounts/chatroom.html", locals())


@login_required
def publish_news(request):
    news_form = NewsForm(request.POST or None, request.FILES)

    if request.POST:
        post = True
        done = False
        if news_form.is_valid():
            title = news_form.cleaned_data["title"]
            subtitle = news_form.cleaned_data["subtitle"]
            image = news_form.cleaned_data["image"]
            content = news_form.cleaned_data["content"]

            news = News()
            news.content = content
            news.image = image
            news.title = title
            news.subtitle = subtitle
            news.publisher = request.user.member
            news.save()

            done = True

    return render(request, "accounts/publish_news.html", locals())


def members(request):

    launch_date = 2017
    now_date = int(timezone.now().strftime("%Y"))
    years = list()

    while now_date >= launch_date:
        years.append(now_date)
        now_date -= 1

    all_members = Member.objects.all()
    return render(request, "accounts/members.html", locals())


def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'A user with this username (' + username + ') already exists'
    return JsonResponse(data)


@login_required
def member_profile(request, id_user=1):

    try:
        member = Member.objects.get(pk=id_user)
        uploads = member.news_set.count() + member.article_set.count() + member.challenge_uploader.count()
        return render(request, "accounts/member.html", locals())
    except Member.DoesNotExist:
        return redirect(members)


def generate_email(name, username):
    greetings = "<h2>Hello " + name + " !</h2><br>"
    body = "<p>Your account has been successfully activated.</p>"
    link = "<p>You are able to login to members dashboard <a href ='https://www.allsafeclub.info/accounts/login'>here</a></p>"
    auth = "<p> username : <strong>" + username + "</strong>"
    regards = "<p>AllSafe Team</p> <br><p>Regards,</p>"
    email_body = greetings + body + link + auth + regards
    return email_body


@login_required
def library(request, page=1):

    search = request.GET.get("search", None)
    tags = DocumentCategroie.objects.all()
    if search:
        documents_all = Document.objects.filter(Q(title__icontains=search) | Q(description__icontains=search)).order_by('-upload_date')
    else:
        documents_all = Document.objects.order_by('-upload_date')

    paginator = Paginator(documents_all, 9)

    try:
        documents = paginator.page(page)
    except EmptyPage:
        documents = paginator.page(1)

    return render(request, "accounts/library.html", locals())


@login_required
def upload_document(request):

    document_form = DocumentForm(request.POST or None, request.FILES)
    post = False
    done = False
    if request.POST and request.FILES:
        post = True
        if document_form.is_valid():
            title = document_form.cleaned_data["title"]
            description = document_form.cleaned_data["description"]
            cover_pic = document_form.cleaned_data["cover_pic"]
            file = document_form.cleaned_data["document_file"]
            tags = document_form.cleaned_data["tags"]

            new_doc = Document()
            new_doc.uploader = request.user.member
            new_doc.title = title
            new_doc.description = description
            new_doc.save()
            new_doc.tags = tags
            new_doc.cover_pic = cover_pic
            new_doc.document_file = file
            new_doc.save()
            done = True

    return render(request, "accounts/upload_document.html", locals())

