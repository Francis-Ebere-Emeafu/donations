import csv
from django.http import HttpResponse
from django.contrib import admin

from convention.models import Attendee, Convention, StudentDelegate


@admin.register(Convention)
class ConventionAdmin(admin.ModelAdmin):
    list_display = ['title', 'year', 'venue']

@admin.register(Attendee)
class AttendeeAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'email']


@admin.register(StudentDelegate)
class StudentDelegateAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'phone', 'email', 'school', 'level']
    actions = ['export_data']

    def export_data(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="students.csv"'
        writer = csv.writer(response)
        writer.writerow(['ID', 'Name', 'School', 'Dept', 'Level', 'State', 'Bio'])

        for delegate in StudentDelegate.objects.all():
            writer.writerow([
                delegate.id,
                '{} {}'.format(delegate.first_name.encode('utf-8'), delegate.last_name.encode('utf-8')),
                delegate.school.encode('utf-8'),
                delegate.department.encode('utf-8'),
                delegate.level.encode('utf-8'),
                delegate.state.encode('utf-8'),
                delegate.extra_info.encode('utf-8')])

        return response
    export_data.short_description = 'Export Student Data'
