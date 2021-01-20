from django.conf.urls import url

from volunteer import views


urlpatterns = [
    url(r'^volunteers/$', views.volunteer, name="volunteer"),
    url(r'^committees/$', views.committee_list, name="committees"),
]
