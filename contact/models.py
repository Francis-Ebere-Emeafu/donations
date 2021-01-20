from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    content = models.TextField()
    message_date = models.DateField(default=timezone.now)

    def __unicode__(self):
        return self.name
