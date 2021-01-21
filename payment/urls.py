from django.conf.urls import url
from django.urls import include, path

from payment import views


urlpatterns = [
    path('transaction/', views.paystack_callback),
]
