from django.conf.urls import url
from django.urls import include, path

from event import views


urlpatterns = [
    path('meetups/', views.meetup_list, name='meetups'),
    path('events/', views.event_list, name='events'),
]
