from django.shortcuts import render

from event.models import Meetup, Event


def meetup_list(request):
    items = Meetup.objects.filter(active=True)
    return render(request, 'event/meetups.html', {'items': items})


def event_list(request):
    items = Event.objects.filter(active=True)
    return render(request, 'event/events.html', {'items': items})
