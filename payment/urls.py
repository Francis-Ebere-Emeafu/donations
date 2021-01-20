from django.conf.urls import url

from payment import views


urlpatterns = [
    url(r'transaction/$', views.paystack_callback),
]
