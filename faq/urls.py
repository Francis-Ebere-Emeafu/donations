from django.conf.urls import url
from django.urls import include, path

from faq import views


urlpatterns = [
    path('faq/', views.questions, name='faq'),
]
