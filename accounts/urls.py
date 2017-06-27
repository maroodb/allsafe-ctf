from django.conf.urls import url

from accounts.views import *

urlpatterns = [

    url(r'^login/', login),
    url(r'^dashboard/', dashboard),
    url(r'^myprofile/', my_profile),

]
