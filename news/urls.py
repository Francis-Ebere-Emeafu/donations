from django.conf.urls import url

from news import views


urlpatterns = [
    url(r'^news/$', views.news_list, name='news_items'),
    url(r'^detail/(?P<id>\d+)/$', views.news_detail, name='news_detail'),
]
