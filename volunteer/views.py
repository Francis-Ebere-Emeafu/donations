from django.shortcuts import render
from volunteer.models import Volunteer, Activity, Committee


def volunteer(request):
    volunteers = Volunteer.objects.all()
    activities = Activity.objects.all()
    return render(
        request,
        'volunteer/volunteer.html',
        {
            'volunteers': volunteers,
            'activities': activities
        }
    )


def committee_list(request):
    committees = Committee.objects.all()
    return render(
        request,
        'volunteer/committees.html',
        {
            'items': committees
        }
    )
