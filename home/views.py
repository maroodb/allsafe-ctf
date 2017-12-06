import requests
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django_ajax.decorators import ajax

from blog.models import News, Award
from design.models import Slide
from home.forms import ContactForm
from home.models import Visitor, Contact
from members.models import Member
from projects.models import ProjectCategory, Project
from itertools import chain


def home(request):
    # Tracking visitor
    visited = False
    if request.session.get('visited', False):
        visited = True
    else:
        request.session["visited"] = True
        visitor = Visitor()
        visitor.ip, visitor.user_agent_id = request.META["REMOTE_ADDR"], request.META["HTTP_USER_AGENT"]
        visitor.save()
    contact_form = ContactForm()
    slides = Slide.objects.order_by('-date')[:5]
    members = Member.objects.filter(user__is_active=True)
    projects_filters = ProjectCategory.objects.all()
    projects = list()
    for category in projects_filters:
        list_of_this = Project.objects.filter(project_category__category_name=category.category_name)[:2]
        projects = list(chain(projects, list_of_this))

    news = News.objects.order_by('-date')[:3]

    members_count = members.count()
    projects_count = Project.objects.count()
    visitors_count = Visitor.objects.count()
    awards_count = Award.objects.count()
    return render(request, "home/index.html", locals())


def contact(request):
    contact_form = ContactForm()
    return render(request, "home/contacts.html", locals())


def team(request):
    staff = Member.objects.filter(user__is_staff=True, user__is_active=True)
    members = Member.objects.filter(user__is_staff=False, user__is_active=True)
    return render(request, "home/team.html", locals())


@ajax
def feedback(request):

    name = request.POST.get("name")
    email = request.POST.get("email")
    subject = request.POST.get("subject")
    message = request.POST.get("message")

    valcaptcha = request.POST.get("g-recaptcha-response")

    url = 'https://www.google.com/recaptcha/api/siteverify'
    data = {
        'secret': '6LdCnhUUAAAAACehzbK9SI9maF9Yfs9KsLfRlytN',
        'response': valcaptcha,
    }

    r = requests.post(url, data)
    result = r.json()
    success = result["success"]
    registered = False

    if success:
        new_contact = Contact()
        new_contact.message = message
        new_contact.subject = subject
        new_contact.name = name
        new_contact.email = email

        new_contact.save()
        registered = True

    response = {
        'robot': not success,
        'registered': registered

    }
    return JsonResponse(response)


def about(request):
    return render(request, "home/about.html", locals())


def fcee7ch1(request):
    return render(request, "home/fcee7ch1.html", locals())


def fcee7ch2(request):
    return render(request, "home/fcee7ch2.html", locals())