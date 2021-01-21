from django.conf.urls import url
from django.urls import include, path
from volunteer import views


urlpatterns = [
    path('volunteers/', views.volunteer, name="volunteer"),
    path('committees/', views.committee_list, name="committees"),
]
