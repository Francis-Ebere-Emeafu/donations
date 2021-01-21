from django.conf.urls import url
from django.urls import include, path

from accounts import views


urlpatterns = [
    path('registration/', views.register, name='register'),
    path('renewal/', views.renew, name='renewal'),
    path('myid/', views.myid, name='myid'),
    path('bankdetails/', views.bank, name="bank_details"),
    path('profile/', views.profile, name="profile"),
]
