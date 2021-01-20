from django.conf.urls import url


from accounts import views


urlpatterns = [
    url(r'registration/$', views.register, name='register'),
    url(r'renewal/$', views.renew, name='renewal'),
    url(r'myid/$', views.myid, name='myid'),
    url(r'bankdetails/$', views.bank, name="bank_details"),
    url(r'profile/$', views.profile, name="profile"),
]
