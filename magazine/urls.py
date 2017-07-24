from django.conf.urls import url

from magazine.views import home

urlpatterns = [


    url(r'^$', home),


]