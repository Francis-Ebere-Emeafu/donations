from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.


class Convention(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    venue = models.CharField(max_length=255)
    details = models.TextField()
    active = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title


class Attendee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=75)
    address = models.TextField(blank=True)
    bio = models.TextField(blank=True)

    def __unicode__(self):
        return self.first_name


def upload_location(instance, filename):
    # filebase, extension = filename.split(".")
    # return "%s/%s.%s" %(instance.id, instance.id, extension)
    return "%s/%s-%s-%s" % ('delegates', instance.phone, instance.first_name, filename)


class StudentDelegate(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=80)
    school = models.CharField(max_length=100)
    department = models.CharField(max_length=150)
    level = models.CharField(max_length=20)
    image = models.ImageField(upload_to=upload_location, null=True, blank=True)
    state = models.CharField(max_length=50)
    address = models.TextField(blank=True)
    extra_info = models.TextField(blank=True)
    when = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.first_name

    class Meta:
        verbose_name_plural = 'Students delegate'
        # return '{}, delegate from {}'.format(self.first_name, self.school)
