from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.utils import timezone
from random import sample
import hashlib
import os
import requests
import json
import logging

logger = logging.getLogger(__name__)

# from payment.forms import PaymentForm
from payment.models import Transaction
from accounts.models import Renewal
from core import utils

PAYSTACK_TEST_KEY = "sk_test_344e71bb214f89cbe8b3b184691f3cba2f556c27"
PAYSTACK_LIVE_KEY = "sk_live_fda55c6950d9727bf9b9255002c355409ac28cad"
PAYSTACK_URL = "https://api.paystack.co/transaction/initialize"
PAYSTACK_KEY = PAYSTACK_LIVE_KEY
VERIFY_URL = "https://api.paystack.co/transaction/verify/{}"


class CouldNotProcess(Exception):
    pass


class NoEmailAddress(Exception):
    pass


def get_reference():
    prefix = "".join(sample("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", 5))
    # prefix = filter(str.isalnum, str(estate.name))[:5]
    suffix = hashlib.md5(os.urandom(32)).hexdigest()[:24]
    return "{}{}".format(prefix, suffix)


def get_payment_url(reference, amount, email):
    key = PAYSTACK_KEY
    url = PAYSTACK_URL
    headers = {
        "Authorization": "Bearer {}".format(key),
        "Content-Type": "application/json",
    }
    payload = {"reference": reference, "amount": amount, "email": email}
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code in [200, 201]:
        data = json.loads(response.content)
        url = data["data"]["authorization_url"]
        return url


def initiate_payment(value, email, account=None, gift=None, renewal=False):
    if not email:
        raise NoEmailAddress
    reference = get_reference()
    if account:
        payment_type = Transaction.DUES
    else:
        payment_type = Transaction.DONATION
    # units = int(naira_value / settings.SMS_COST)
    Transaction.objects.create(
        amount=value,
        account=account,
        gift=gift,
        renewal=renewal,
        reference=reference,
        payment_type=payment_type,
        status=Transaction.PENDING,
    )
    amt = int(value * 100)
    url = get_payment_url(reference, amt, email)
    if not url:
        raise CouldNotProcess
    return url


def paystack_callback(request):
    trxref = request.GET.get("trxref")
    logger.info("request with transaction ref {}".format(trxref))
    logger.info("verifying transaction...")

    key = PAYSTACK_KEY
    url = VERIFY_URL.format(trxref)
    headers = {
        "Authorization": "Bearer {}".format(key),
        "Content-Type": "application/json",
    }
    response = requests.get(url, headers=headers)
    logger.info(str(response.content))
    try:
        status = json.loads(response.content)["data"]["status"]
    except KeyError:
        return False
    else:
        transaction = get_object_or_404(Transaction, reference=trxref)
        if status == "success":
            transaction.status = Transaction.SUCCESS
            transaction.save()
            acct = transaction.account
            gift = transaction.gift
            if acct:
                if transaction.renewal:
                    today = timezone.now().date()
                    Renewal.objects.create(account=acct, payment_date=today)
                    payment_due_date = acct.next_payment_due
                    if payment_due_date:
                        next_payment_due = payment_due_date.replace(
                            year=payment_due_date.year + 1
                        )
                    else:
                        next_payment_due = today.replace(year=today.year + 1)
                    acct.next_payment_due = next_payment_due
                    acct.save()
                    utils.queue_mail(
                        "renewal_email",
                        [acct.email],
                        {"account": acct, "amount": transaction.amount},
                    )
                    messages.success(
                        request, "Your payment has been processed successfully"
                    )
                else:
                    today = timezone.now().date()
                    acct.paid = True
                    acct.membership_number = utils.get_membership_number()
                    acct.next_payment_due = today.replace(year=today.year + 1)
                    acct.save()
                    messages.success(
                        request, "Your payment has been processed successfully"
                    )
                    # send mail
                    subject = "ASN: Your registration is being confirmed."
                    message = "Thank you for joining Atheist Society of Nigeria. We are glad to have you"
                    html_message = render_to_string(
                        "asn_welcome.html",
                        {
                            "applicant_name": acct.first_name,
                            "amount": transaction.amount,
                            "receive_email": acct.email,
                        },
                    )
                    send_mail(
                        subject,
                        message,
                        "registrations@atheist.org.ng",
                        [acct.email],
                        fail_silently=False,
                        html_message=html_message,
                    )
                return redirect("thanks")
            if gift:
                gift.paid = True
                gift.save()
                messages.success(
                    request, "Your payment has been processed successfully"
                )
                return redirect("thanks_donation")
        else:
            transaction.status = Transaction.FAILURE
            transaction.save()
            messages.error(
                request,
                "There was an error processing your request. Please contact your financial institution to verify that you were not debited",
            )
            return redirect("thanks_error")
