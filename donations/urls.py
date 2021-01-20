"""donations URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

from accounts import views as accounts_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("tinymce/", include("tinymce.urls")),

    path('pages/', include('django.contrib.flatpages.urls')),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('vision/mission/', TemplateView.as_view(template_name='account/vision_mission.html'), name='vision_mission'),
    # path('meetups/$', meetup_views.meetup_list, name='meetups'),
    path('donate/', accounts_views.make_gift, name='make_gift'),
    path('bot/', TemplateView.as_view(template_name='bot.html'), name='bot'),
    path('thanks/', TemplateView.as_view(template_name='thanks.html'), name='thanks'),
    path('thanks_donor/', TemplateView.as_view(template_name='thanks_donation.html'), name='thanks_donation'),
    path('thanks_error/', TemplateView.as_view(template_name='thanks_error.html'), name='thanks_error'),
    # path('contact/$', contact, name='contact'),
    path('mission/', TemplateView.as_view(template_name='vision.html'), name='mission'),
    path('future/', TemplateView.as_view(template_name='future.html'), name='future'),
    path('executives/', TemplateView.as_view(template_name='executives.html'), name='executives'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path("about", TemplateView.as_view(template_name="about.html"), name="about"),


    path('accounts/', include("accounts.urls")),
    path('volunteer/', include("volunteer.urls")),
    path('event/', include("event.urls")),
    path('faq/', include("faq.urls")),
    path('news/', include("news.urls")),
    path('contact/', include("contact.urls")),
    path('convention/', include("convention.urls")),
    path('payment/', include("payment.urls")),
]


admin.site.site_header = 'Atheist Society of Nigeria Admin'


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
