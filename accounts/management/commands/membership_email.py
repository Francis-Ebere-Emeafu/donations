from django.core.management.base import BaseCommand

#from dateutil import parser

#from order.models import Item, Order
#from location.models import Location
from accounts.models import Account
from core import utils


class Command(BaseCommand):
    help = '''Send membership email to paid-up members.'''

    def handle(self, *args, **kwargs):
        accts = Account.objects.filter(paid=True, membership_email_sent=False)

        for acct in accts:
            if not acct.certificate:
                self.stdout.write('No certificate for {}'.format(acct.full_name))
                continue
            utils.send_membership_mail(acct)
            acct.membership_email_sent = True
            acct.save()
            self.stdout.write('Sent mail to {}'.format(acct.full_name))
        self.stdout.write('Done sending membership emails')
