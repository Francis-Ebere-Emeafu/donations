from convention import views
from django.conf.urls import url
from django.urls import include, path

from django.views.generic import TemplateView



urlpatterns = [
    path('details/', views.convention_page, name='convention'),
    path('students/delegate/', views.student_delegate, name='delegate'),
    path('students/delegate/confirmation/', TemplateView.as_view(template_name='convention/confirmation.html'), name='confirmation'),
    path('speakers/', TemplateView.as_view(template_name='convention/speakers.html'), name='speakers'),
    path('programme/', TemplateView.as_view(template_name='convention/programme.html'), name='programme'),
    path('venue/', TemplateView.as_view(template_name='convention/venue.html'), name='venue'),
]
