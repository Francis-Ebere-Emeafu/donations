from django.contrib import admin

from volunteer.models import Volunteer, Activity, Committee


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['summary', 'details']


@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']


@admin.register(Committee)
class CommitteeAdmin(admin.ModelAdmin):
    list_display = ['title', 'brief']
