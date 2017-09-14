from django.conf.urls import url

from events.views import event

urlpatterns = [

    url(r'^event/', event),



]
