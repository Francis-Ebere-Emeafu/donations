from django import forms

from payment.models import Transaction


class PaymentForm(forms.ModelForm):

    class Meta:
        model = Transaction
