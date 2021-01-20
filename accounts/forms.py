from django import forms
from django.contrib.auth.models import User
from accounts.models import Account, Gift, GiftOptions

PAYMENT_TYPES = [
    (0, 'Bank Hold'),
    (1, 'Debit card/Online Transfer'),
]


class AccountRegisterForm(forms.ModelForm):
    payment_type = forms.CharField(
        widget=forms.RadioSelect(choices=PAYMENT_TYPES))

    class Meta:
        model = Account
        exclude = ['city', 'paid', 'when']

    def clean_email(self):
        if 'email' in self.cleaned_data:
            try:
                User.objects.get(username=self.cleaned_data['email'])
            except User.DoesNotExist:
                return self.cleaned_data['email']
            else:
                raise forms.ValidationError('An account with this email already exists')


class GiftForm(forms.ModelForm):
    payment_type = forms.CharField(
        widget=forms.RadioSelect(choices=PAYMENT_TYPES))

    #gift_option = forms.ModelChoiceField(
    #    queryset=GiftOptions.objects.all(),
    #    widget=forms.RadioSelect,
    #    empty_label=None, required=False)
    #amount = forms.DecimalField(max_digits=10, decimal_places=2, required=False)

    class Meta:
        model = Gift
        exclude = ['when']


class RenewalForm(forms.Form):
    account = forms.CharField(max_length=20)

    def clean_account(self):
        if 'account' in self.cleaned_data:
            _acct = self.cleaned_data['account'][5:]
            #import pdb;pdb.set_trace()
            try:
                acct = Account.objects.get(membership_number=_acct)
            except Account.DoesNotExist:
                raise forms.ValidationError(
                    '''Sorry your membership number is invalid. Please
                    check to make sure it is correct and try again.''')
            else:
                return acct


class IDForm(forms.Form):
    email = forms.CharField(max_length=100)

    def clean_email(self):
        #import pdb;pdb.set_trace()
        if 'email' in self.cleaned_data:
            try:
                acct = Account.objects.get(
                    email__iexact=self.cleaned_data['email'], paid=True)
            except Account.DoesNotExist:
                raise forms.ValidationError(
                    '''Sorry the email you entered is not in our database.
                    Please check to make sure it is correct and try again.''')
            else:
                return acct.member_id
