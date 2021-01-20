from convention import views
from django.conf.urls import url
from django.views.generic import TemplateView



urlpatterns = [
    url(r'^details/$', views.convention_page, name='convention'),
    url(r'^students/delegate/$', views.student_delegate, name='delegate'),
    url(r'^students/delegate/confirmation$', TemplateView.as_view(template_name='convention/confirmation.html'), name='confirmation'),
    url(r'^speakers/$', TemplateView.as_view(template_name='convention/speakers.html'), name='speakers'),
    url(r'^programme/$', TemplateView.as_view(template_name='convention/programme.html'), name='programme'),
    url(r'^venue/$', TemplateView.as_view(template_name='convention/venue.html'), name='venue'),
]
