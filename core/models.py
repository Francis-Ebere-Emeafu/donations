from __future__ import unicode_literals

from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20)
    dial_code = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'Countries'

    def __unicode__(self):
        return '{} (+{})'.format(self.name, self.dial_code)
