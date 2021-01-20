import csv
from django.contrib import admin
from django.http import HttpResponse

# Register your models here.
from accounts.models import Account, Gift, Membership, GiftOptions
from core import utils


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = [
        "first_name",
        "last_name",
        "email",
        "member_id",
        "when",
        "phone",
        "membership",
        "paid",
        "membership_email_sent",
        "next_payment_due",
    ]
    list_filter = ["paid", "membership_email_sent"]
    search_fields = ["first_name", "last_name", "email"]
    # actions = ['mark_as_paid', 'mark_as_not_paid']
    actions = ["export_data", "export_payment_data", "mark_as_paid"]

    def mark_as_paid(self, request, queryset):
        queryset.update(paid=True)

    mark_as_paid.short_description = "Mark as Paid"

    def mark_as_not_paid(self, request, queryset):
        queryset.update(paid=False)

    mark_as_not_paid.short_description = "Mark as NOT Paid"

    def save_model(self, request, obj, form, change):
        if not obj.membership_number and obj.paid:
            obj.membership_number = utils.get_membership_number()
        obj.save()

    def export_data(self, request, queryset):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="members.csv"'
        writer = csv.writer(response)
        writer.writerow(
            ["First Name", "Last Name", "Email", "Phone", "address", "date_registered"]
        )

        for acct in queryset:
            writer.writerow(
                [
                    acct.first_name.encode("utf-8"),
                    acct.last_name.encode("utf-8"),
                    acct.email.encode("utf-8"),
                    acct.phone.encode("utf-8"),
                    acct.address.encode("utf-8"),
                    acct.when.strftime("%d-%m-%Y"),
                ]
            )
        return response

    export_data.short_description = "Export Members Data"

    def export_payment_data(self, request, queryset):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="members.csv"'
        writer = csv.writer(response)
        writer.writerow(["First Name", "Last Name", "Email", "Phone", "next_payment"])

        for acct in queryset:
            writer.writerow(
                [
                    acct.first_name.encode("utf-8"),
                    acct.last_name.encode("utf-8"),
                    acct.email.encode("utf-8"),
                    "Phone: {}".format(acct.phone.encode("utf-8")),
                    format(acct.next_payment_due.strftime("%d-%b-%Y")),
                ]
            )
        return response

    export_payment_data.short_description = "Export Payment Information"

    def send_telegram_invite(self, request, queryset):
        from django.core.mail import send_mail

        subject = "New ASN Telegram group"
        message = "<p>Dear {},</p><p>We are pleased to inform you that the Atheist Society of Nigeria now as a telegram group for members of the society.</p><p>This group was created so that we can keep abreast of the plans and activities of the society as well as get quick feedback on questions and issues we may have.</p><p>Just click on <a href='https://t.me/joinchat/DUYr0REhxw6yhqvghiCzBw'>ASN Group Link</a> to join.</p><p>Thank You</p>"
        for member in queryset:
            send_mail(
                subject,
                message.format(member.first_name),
                "info@atheist.org.ng",
                [member.email],
                html_message=message.format(member.first_name),
            )

    send_telegram_invite.short_description = "Send Invites to Telegram Group"


@admin.register(GiftOptions)
class GiftOptionAdmin(admin.ModelAdmin):
    list_display = ["amount", "dollar_value"]


@admin.register(Gift)
class GiftAdmin(admin.ModelAdmin):
    list_display = [
        "first_name",
        "last_name",
        "amount",
        "when",
        "email",
        "phone",
        "country",
        "paid",
    ]


@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "dues"]


# admin.site.disable_action('delete_selected')
