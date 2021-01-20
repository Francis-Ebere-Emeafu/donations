from django.core.management.base import BaseCommand

#from dateutil import parser

#from order.models import Item, Order
#from location.models import Location
from accounts.models import Account
from core import edit_cert
#from core import utils


class Command(BaseCommand):
    help = '''Generate certificates for paid-up members.'''

    def handle(self, *args, **kwargs):
        accts = Account.objects.filter(paid=True, membership_email_sent=False)

        for acct in accts:
            if not acct.certificate:
                fname = '{}_{}.png'.format(
                    acct.first_name.lower(), acct.last_name.lower())
                regno = acct.member_id
                name = acct.full_name
                dt = acct.when.strftime('%b %Y')
                fpath = edit_cert.paint_cert(regno, name, dt, fname)
                if fpath:
                    acct.certificate.name = 'certificates/{}'.format(fname)
                    acct.save()
                self.stdout.write('Certificate for {}'.format(acct.full_name))
                continue
            #utils.send_membership_mail(acct)
            #acct.membership_email_sent = True
            #acct.save()
            #self.stdout.write('Sent mail to {}'.format(acct.full_name))
        self.stdout.write('Done generating certificates')
