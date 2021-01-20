from django.core.management.base import BaseCommand
from django.utils import timezone

# from dateutil import parser

# from order.models import Item, Order
# from location.models import Location
from accounts.models import Account
from core import utils


class Command(BaseCommand):
    help = """Send emails for renewals"""

    def handle(self, *args, **kwargs):
        today = timezone.now().date()
        # next_month = today + timezone.timedelta(31)
        # accts = Account.objects.filter(
        #    paid=True,
        #    next_payment_due__gt=today,
        #    next_payment_due__lt=next_month)
        # for acct in accts:
        #    utils.queue_mail(
        #        'renewal_almost_due',
        #        acct.email,
        #        {'account': acct},
        #        from_email='membership@atheist.org.ng')

        late = Account.objects.filter(paid=True, next_payment_due__lt=today)
        for acct in late:
            utils.queue_mail(
                "renewal_past",
                acct.email,
                {"account": acct},
                from_email="membership@atheist.org.ng",
            )
