from django.contrib import admin

from contact.models import ContactMessage


@admin.register(ContactMessage)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message_date']
