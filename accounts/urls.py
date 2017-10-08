from django.conf.urls import url, include

from accounts.views import *
from library.views import document_details

urlpatterns = [

    url(r'^login/', login_view, name='login'),
    url(r'^dashboard/', dashboard),
    url(r'^admin/active', account_management),
    url(r'^admin/', administration),
    url(r'^myprofile/', my_profile),
    url(r'^signup/', signup),
    url(r'^logout/', deconnect),
    #url(r'^inbox/', inbox),
    url(r'^chatroom/', chatroom),
    url(r'^publish/news/', publish_news),
    url(r'^ajax/validate_username/$', validate_username, name='validate_username'),
    url(r'^members/$', members),
    url(r'^library/$', library),
    url(r'^library/upload', upload_document),
    url(r'^library/(?P<page>\d+)$', library, name='documents_list'),
    url(r'^library/documents/(?P<doc_id>\d+)$', document_details, name='document_details'),
    url(r'^members/profile/(?P<id_user>\d+)$', member_profile),

]
