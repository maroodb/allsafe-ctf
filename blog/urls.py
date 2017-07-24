from django.conf.urls import url

from blog.views import blog, news

urlpatterns = [

    url(r'^$', blog),
    url(r'^(?P<page>\d+)$', blog, name='news_list'),
    url(r'^news/(?P<id_news>\d+)$', news, name='news')

]
