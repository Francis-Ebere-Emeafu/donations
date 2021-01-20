from __future__ import unicode_literals

from django.db import models


class Meetup(models.Model):
    location = models.CharField(max_length=200)
    meetup_date = models.DateField()
    contact_name = models.CharField(max_length=200)
    contact_phone = models.CharField(max_length=20)
    active = models.BooleanField(default=False)

    def __unicode__(self):
        return self.location


class Event(models.Model):
    title = models.CharField(max_length=200)
    kind = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    organisers = models.CharField(max_length=200)
    entry_fee = models.DecimalField(max_digits=10, decimal_places=2)
    venue = models.TextField()
    details = models.TextField()
    active = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title


