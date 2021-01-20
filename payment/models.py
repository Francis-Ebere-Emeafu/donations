from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

from accounts.models import Account
from accounts.models import Gift


class Transaction(models.Model):
    PENDING = 0
    INITIATED = 1
    SUCCESS = 2
    FAILURE = 3
    STATUSES = enumerate(('Pending', 'Initiated', 'Success', 'Failure'))

    NGN = 0
    USD = 1
    CURRENCY = enumerate(('NGN', 'USD'))

    DONATION = 0
    DUES = 1

    PAYMENT_TYPES = enumerate(('Donation', 'Dues'))

    # estate = models.ForeignKey(Estate)
    account = models.ForeignKey(Account, null=True, on_delete=models.SET_NULL)
    gift = models.ForeignKey(Gift, null=True, on_delete=models.SET_NULL)

    # amount in naira
    amount = models.PositiveIntegerField()

    # amount in currency of transaction
    reference = models.CharField(max_length=100, unique=True)
    started = models.DateTimeField(default=timezone.now)
    concluded = models.DateTimeField(null=True, blank=True)
    status = models.PositiveIntegerField(choices=STATUSES)
    payment_type = models.PositiveIntegerField(choices=PAYMENT_TYPES)
    renewal = models.BooleanField(default=False)

    def __unicode__(self):
        return self.reference
