from django.core.management.base import BaseCommand

from django.core.mail import send_mail
from django.template.loader import render_to_string

from accounts.models import Account
from core import utils


class Command(BaseCommand):
    help = '''Send mails to members yet to complete their registration'''

    def handle(self, *args, **kwargs):
        accts = Account.objects.filter(paid=False, membership_email_sent=False, membership_number__isnull=True)
        print(accts)

        subject = 'ASN: How may we help you complete your ASN registration'
        message = 'ASN Support: discovered that you have not completed the registration process you initiated'
        # html_message = render_to_string('complete_registration.html', {
        #     'account': acct
        # })

        for acct in accts:
            print("mail sent to {}'s email: {}".format(acct.first_name, acct.email))

            # using django send mail function
            html_message = render_to_string('complete_registration.html', {
            'account': acct
            })
            send_mail(
                subject,
                message,
                'registrations@atheist.org.ng',
                [acct.email, 'freemandigits@gmail.com'],
                fail_silently=False,
                html_message=html_message
            )

            # using post-office send mail function
            utils.queue_mail(
                "complete_membership",
                acct.email,
                {"account": acct},
                from_email="registration@atheist.org.ng",
            )
            # acct.paid=False
            # acct.save()
        print("Done sending complete membership mail to registrants")
