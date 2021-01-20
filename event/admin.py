from django.contrib import admin

from event.models import Event, Meetup


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'kind', 'venue']


@admin.register(Meetup)
class MeetupAdmin(admin.ModelAdmin):
    list_display = ['location', 'meetup_date', 'contact_name', 'contact_phone']
