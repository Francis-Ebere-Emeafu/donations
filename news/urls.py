from django.conf.urls import url
from django.urls import include, path

from news import views


urlpatterns = [
    path('news/', views.news_list, name='news_items'),
    path('detail/<int:id>/', views.news_detail, name='news_detail'),
]
