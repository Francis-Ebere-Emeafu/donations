from django.contrib import admin

from payment.models import Transaction


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['account', 'amount', 'payment_type', 'status']
    search_fields = ['account__first_name', 'account__last_name', 'account__email']
