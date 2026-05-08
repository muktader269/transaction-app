from django.contrib import admin
from .models import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver_phone', 'amount', 'timestamp')
    list_filter = ('timestamp',)
    search_fields = ('receiver_phone', 'sender__username')