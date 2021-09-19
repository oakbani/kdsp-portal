from django.contrib import admin

# Register your models here.

from .models import Payment


class PaymentAdmin(admin.ModelAdmin):
    list_display = ["therapy_slot", "amount", "status"]

    list_editable = ["status"]


admin.site.register(Payment, PaymentAdmin)
