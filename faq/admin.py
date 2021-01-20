from django.contrib import admin

from faq.models import Question


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['text', 'answer']
