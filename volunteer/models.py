from __future__ import unicode_literals

from django.db import models


class Activity(models.Model):
    summary = models.CharField(max_length=200)
    details = models.TextField()

    def __unicode__(self):
        return self.summary

    class Meta:
        verbose_name_plural = 'Activities'


class Volunteer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    detail = models.TextField()

    def __unicode__(self):
        return self.name


class Committee(models.Model):
    title = models.CharField(max_length=200)
    brief = models.TextField()
    member_count = models.PositiveIntegerField(default=0)

    def __unicode__(self):
        return self.title

    @property
    def members(self):
        return self.member_count
