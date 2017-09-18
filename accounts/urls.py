from django.conf.urls import url, include

from accounts.views import *

urlpatterns = [

    url(r'^login/', login_view, name='login'),
    url(r'^dashboard/', dashboard),
    url(r'^admin/', administration),
    url(r'^myprofile/', my_profile),
    url(r'^signup/', signup),
    url(r'^logout/', deconnect),
    #url(r'^inbox/', inbox),
    url(r'^chatroom/', chatroom),
    url(r'^publish/news/', publish_news),
    url(r'^ajax/validate_username/$', validate_username, name='validate_username'),
    url(r'^members/$', members),
    url(r'^members/profile/(?P<id_user>\d+)$', member_profile),

]
