from django.conf.urls import url

from magazine.views import home, newslettre

urlpatterns = [


    url(r'^$', home),
    url(r'^newslettre/', newslettre)


]