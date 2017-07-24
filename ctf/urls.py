from django.conf.urls import url

from ctf.views import scoreboard, upload

urlpatterns = [

    url(r'^scoreboard/', scoreboard),
    url(r'^upload/', upload),


]
