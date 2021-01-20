from django.conf.urls import url

from faq import views


urlpatterns = [
    url(r'^faq/$', views.questions, name='faq'),
]
