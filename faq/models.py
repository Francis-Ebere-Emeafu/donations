from __future__ import unicode_literals

from django.db import models


class Question(models.Model):
    text = models.CharField(max_length=250)
    answer = models.TextField()

    def __unicode__(self):
        return self.text
