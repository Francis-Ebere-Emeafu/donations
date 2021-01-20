from django.contrib import admin

from news.models import NewsPost
from news.forms import NewsForm


@admin.register(NewsPost)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'reference_date', 'publish_date', 'active']
    form = NewsForm
