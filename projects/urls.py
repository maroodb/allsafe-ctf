from django.conf.urls import url

from projects.views import project_list, project_details

urlpatterns = [
    url(r'^$', project_list),
    url(r'^(?P<page>\d+)$', project_list, name='projects_list'),
    url(r'^item/(?P<id_project>\d+)$', project_details, name='project_details')
]
