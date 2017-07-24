from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django_ajax.decorators import ajax

from blog.models import News
from design.models import Slide
from home.forms import ContactForm
from home.models import Visitor
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
    members = Member.objects.all()
    projects_filters = ProjectCategory.objects.all()
    projects = list()
    for category in projects_filters:
        list_of_this = Project.objects.filter(project_category__category_name=category.category_name)[:2]
        projects = list(chain(projects, list_of_this))

    news = News.objects.order_by('-date')[:3]

    members_count = members.count()
    projects_count = Project.objects.count()
    visitors_count = Visitor.objects.count()
    return render(request, "home/index.html", locals())


def contact(request):
    return render(request, "home/contacts.html", locals())


def team(request):
    members = Member.objects.all()
    return render(request, "home/team.html", locals())


@ajax
def feedback(request):
    tes = "yes"
    return HttpResponse(tes)


def about(request):
    return render(request, "home/about.html", locals())
