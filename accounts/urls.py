from django.conf.urls import url, include

from accounts.views import *

urlpatterns = [

    url(r'^login/', login_view),
    url(r'^dashboard/', dashboard),
    url(r'^myprofile/', my_profile),
    url(r'^signup/', signup),
    url(r'^logout/', logout),



]
