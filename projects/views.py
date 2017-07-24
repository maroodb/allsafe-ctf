from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render, redirect

from projects.models import Project, ProjectCategory


def project_list(request, page=1):
    all_projects = Project.objects.order_by('-date_end')
    projects_filters = ProjectCategory.objects.all()
    paginator = Paginator(all_projects, 9)

    try:
        projects = paginator.page(page)
    except EmptyPage:
        projects = paginator.page(paginator.num_pages)

    return render(request, "projects/portfolio.html", locals())


def project_details(request, id_project):
    try:
        target_project = Project.objects.get(pk=id_project)
    except Project.DoesNotExist:
        return redirect('/projects')

    return render(request, "projects/project.html", locals())
