from django.conf.urls import url

from ctf.views import scoreboard, upload, challenges, ctf_resolve, challenge_details

urlpatterns = [

    url(r'^scoreboard/', scoreboard),
    url(r'^upload/', upload),
    url(r'^challenges/$', challenges),
    url(r'^challenges/(?P<id_ch>\d+)$', challenge_details, name='challenge_details'),
    url(r'^submit/(?P<id_ch>\d+)$', ctf_resolve, name='resolve_challenge'),



]
