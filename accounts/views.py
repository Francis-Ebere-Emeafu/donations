from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from accounts.forms import AccountRegisterForm, GiftForm, RenewalForm, IDForm
from accounts.models import Account, Gift

from payment.views import initiate_payment, CouldNotProcess, NoEmailAddress

# Create your views here.


# def register(request):
#     if request.method == 'POST':
#         registration_form = RegistrationForm(request.POST)
#         if registration_form.is_valid():
#             username = registration_form.cleaned_data['username']
#             email = registration_form.cleaned_data['email']
#             password = registration_form.cleaned_data['password1']
#             usr = User.objects.create_user(
#                 username=email, password=password)

#             # authenticate and login
#             newuser = authenticate(username=email, password=password)

#             if newuser:
#                 login(request, newuser)
#                 return redirect('profile')

#     else:
#         registration_form = RegistrationForm()
#     return render(
#         request,
#         'account/register.html',
#         {'registration_form': registration_form})


def myid(request):
    membership_id = None
    if request.method == 'POST':
        form = IDForm(request.POST)
        if form.is_valid():
            membership_id = form.cleaned_data['email']
    else:
        form = IDForm()
    return render(request, 'account/id.html', {'form': form, 'id': membership_id})


def renew(request):
    if request.method == 'POST':
        form = RenewalForm(request.POST)
        if form.is_valid():
            acct = form.cleaned_data['account']
            amount = acct.membership.dues
            email = acct.email
            try:
                payment_url = initiate_payment(
                    amount, email, account=acct, renewal=True)
            except CouldNotProcess:
                messages.error(
                    request,
                    'We cannot process your payment. Please use another means')
            else:
                return redirect(payment_url)
    else:
        form = RenewalForm()
    return render(request, 'account/renewal.html', {'form': form})


def register(request):
    # import pdb;pdb.set_trace()
    if request.method == 'POST':
        form = AccountRegisterForm(request.POST)
        if form.is_valid():
            member = form.save()
            recieve_email = member.email
            # messages.success(
            #    request,
            #    'Application received. Pay to complete your registration!')
            if member.payment_type == Account.BANK_TRANSFER:
                subject = 'ASN: Make payment to complete your registration'
                message = 'Bank: Access Bank, Account Number: 0739048315, Account Name: Atheist Society of Nigeria'
                html_message = render_to_string('bank_details.html', {
                    'applicant_name': member.first_name,
                    'amount': member.membership.dues,
                    'recieve_email': recieve_email
                })
                send_mail(
                    subject,
                    message,
                    'registrations@atheist.org.ng',
                    [recieve_email, 'registrations@atheist.org.ng'],
                    fail_silently=False,
                    html_message=html_message
                )
                return redirect('bank_details')
            elif member.payment_type == Account.DEBIT_CARD:
                amount = member.membership.dues
                email = member.email
                subject = 'ASN: Your registration is being confirmed.'
                message = 'Thank you for joining Atheist Society of Nigeria. We are glad to have you'
                html_message = render_to_string('asn_welcome.html', {
                    'applicant_name': member.first_name,
                    'amount': member.membership.dues,
                    'recieve_email': recieve_email
                })
                try:
                    payment_url = initiate_payment(
                        amount, email, account=member, renewal=False)
                except NoEmailAddress:
                    messages.error(
                        request,
                        'We cannot see your email address. Please use another means')
                except CouldNotProcess:
                    messages.error(
                        request,
                        'We cannot process your payment. Please use another means')
                else:
                    ## Payment email is sent after verification
                    #send_mail(
                    #    subject,
                    #    message,
                    #    'registrations@atheist.org.ng',
                    #    [recieve_email],
                    #    fail_silently=False,
                    #    html_message=html_message
                    #)
                    return redirect(payment_url)

    else:
        form = AccountRegisterForm()
    return render(request, 'account/register.html', {'form': form})


def bank(request):
    return render(request, 'account/bank.html', {})


@login_required
def profile(request):
    return render(request, 'account/profile.html', {})


def make_gift(request):
    if request.method == 'POST':
        form = GiftForm(request.POST)
        #import pdb;pdb.set_trace()
        if form.is_valid():
            gift = form.save()
            if gift.payment_type == Gift.BANK_TRANSFER:
                # send mail
                return redirect('bank_details')
            elif gift.payment_type == Gift.DEBIT_CARD:
                amount = gift.amount
                email = gift.email
                # send email
                try:
                    payment_url = initiate_payment(
                        amount, email, gift=gift)
                except NoEmailAddress:
                    messages.error(
                        request,
                        'We cannot process your payment. Please use bank transfer')
                except CouldNotProcess:
                    messages.error(
                        request,
                        'We cannot process your payment. Please use bank transfer')
                else:
                    return redirect(payment_url)
    else:
        form = GiftForm()
        # if gifter.payment_type == Gift.BANK_TRANSFER:
        #     return redirect('bank_details')
        # elif gifter.payment_type == Gift.DEBIT_CARD:

    return render(request, 'register/make_gift.html', {'form': form})


def volunteer(request):
    return render(request, 'register/volunteer.html')
