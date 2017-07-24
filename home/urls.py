from django.conf.urls import url

from home.views import home, contact, team, feedback, about

urlpatterns = [

    url(r'^team/', team),
    url(r'^contact/', contact),
    url(r'^feedback/', feedback),
    url(r'^about/', about),
    url(r'^$', home),


]
