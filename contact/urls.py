from django.conf.urls import url
from django.urls import include, path

from contact import views


urlpatterns = [
    path('contact/', views.message, name='contact'),
]
