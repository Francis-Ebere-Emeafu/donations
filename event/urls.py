from django.conf.urls import url

from event import views


urlpatterns = [
    url(r'^meetups/$', views.meetup_list, name='meetups'),
    url(r'^events/$', views.event_list, name='events'),
]
