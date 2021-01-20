import os
import requests
from requests.auth import HTTPBasicAuth

from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.db.models.aggregates import Max
from django.conf import settings
from post_office import mail

from accounts.models import Account

FROM_EMAIL = 'registrations@atheist.org.ng'

REGISTRATION_BANK = 0
REGISTRATION_DEBIT = 1
DONATION_BANK = 0
DONATION_DEBIT = 1


def queue_mail(mail_template, recipients, context, from_email=FROM_EMAIL):
    mail.send(
        recipients,
        from_email,
        template=mail_template,
        context=context)


def process_mail(kind, to, name, amount):
    if kind == REGISTRATION_BANK:
        subject = 'ASN: Make payment to complete your registration'
        message = 'Bank: Access Bank; Account Number: 0739048315; Account Name: Atheist Society of Nigeria'
        html_message = render_to_string(
            'bank_details.html',
            {
                'applicant_name': name,
                'amount': amount,
                'recieve_email': to
            })
        send_mail(
            subject,
            message,
            FROM_EMAIL,
            [to],
            fail_silently=False,
            html_message=html_message)


def sendsms(to, msg, sender='ASN'):
    if to.startswith('0'):
        to = '234{}'.format(to[-10:])
    payload = {
        'from': sender,
        'to': to,
        'text': msg
    }
    basic_auth = HTTPBasicAuth(settings.SMS_USR, settings.SMS_PWD)
    return requests.post(settings.SMS_URL, json=payload, auth=basic_auth)


def send_membership_mail(acct):
    print('sending mail to {}'.format(acct.full_name))

    subject = 'Your ASN membership Information'
    body = 'Here is your membership information'
    html_message = render_to_string(
        'unique_id.html',
        {
            'receive_email': acct.email,
            'identity_no': acct.member_id,
            'member': acct.full_name,
        })
    msg = EmailMultiAlternatives(
        subject,
        body,
        'membership@atheist.org.ng',
        [acct.email]
    )
    msg.attach_alternative(html_message, 'text/html')
    msg.attach_file(acct.certificate.path)
    constitution_path = os.path.join(settings.STATIC_ROOT, 'constitution.pdf')
    msg.attach_file(constitution_path)
    result = msg.send()

    #result = send_mail(
    #    subject,
    #    body,
    #    'membership@atheist.org.ng',
    #    [acct.email, 'info@atheist.org.ng'],
    #    fail_silently=False,
    #    html_message=html_message)
    print(result)


def get_membership_number():
    max_num = Account.objects.aggregate(
        Max('membership_number'))['membership_number__max']
    return max_num + 1
