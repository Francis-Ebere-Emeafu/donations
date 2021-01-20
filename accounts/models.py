from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
# Create your models here.


class Membership(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    dues = models.DecimalField(max_digits=10, decimal_places=2)

    def __unicode__(self):
        return '{} ({} per annum)'.format(self.name, self.dues)


class Account(models.Model):
    BANK_TRANSFER = 0
    DEBIT_CARD = 1

    PAYMENT_TYPES = enumerate(('Bank Transfer', 'Debit Card'))

    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=20)
    address = models.TextField(blank=True)
    bio = models.TextField(blank=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    when = models.DateTimeField(default=timezone.now)
    membership = models.ForeignKey(Membership, null=True, on_delete=models.SET_NULL)
    payment_type = models.PositiveIntegerField(
        choices=PAYMENT_TYPES, default=DEBIT_CARD)
    paid = models.BooleanField(default=False)
    membership_email_sent = models.BooleanField(default=False)
    membership_number = models.PositiveIntegerField(null=True, blank=True)
    certificate = models.ImageField(
        upload_to='certificates', null=True, blank=True)
    next_payment_due = models.DateField(null=True, blank=True)

    def __unicode__(self):
        return self.email

    @property
    def member_id(self):
        if self.membership_number:
            mem_no = '{:0>4}'.format(self.membership_number)
            yr = self.when.strftime('%y')
            return 'ASN{}{}'.format(yr, mem_no)
            #return 'ASN17{}'.format("{0:0>4}".format(self.membership_number))
        else:
            return 'N/A'

    @property
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)


class GiftOptions(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    dollar_value = models.DecimalField(
        max_digits=20, decimal_places=2, default=0)

    def __unicode__(self):
        return '{} (${})'.format(self.amount, self.dollar_value)

    class Meta:
        verbose_name_plural = 'Gift Options'


class Gift(models.Model):
    BANK_TRANSFER = 0
    DEBIT_CARD = 1

    PAYMENT_TYPES = enumerate(('Bank Transfer', 'Debit card'))

    NGN = 0
    USD = 1
    GBP = 2
    EURO = 3

    CURRENCIES = enumerate(('NGN', 'USD', 'GBP', 'EURO'))

    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=20)
    country = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    #currency = models.PositiveIntegerField(choices=CURRENCIES, default=NGN)
    #gift_option = models.ForeignKey(GiftOptions, null=True)
    when = models.DateTimeField(default=timezone.now)
    bio = models.TextField(blank=True)
    email_sent = models.BooleanField(default=False)
    payment_type = models.PositiveIntegerField(choices=PAYMENT_TYPES, default=BANK_TRANSFER)
    paid = models.BooleanField(default=False)

    def __unicode__(self):
        return self.first_name


class Renewal(models.Model):
    account = models.ForeignKey(Account, null=True, on_delete=models.SET_NULL)
    payment_date = models.DateField()

    def __unicode__(self):
        return unicode(self.account)
