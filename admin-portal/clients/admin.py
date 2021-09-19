from django.contrib import admin

# Register your models here.

from .models import Client


class ClientAdmin(admin.ModelAdmin):
    list_display = ["name", "father_name", "status"]

    # list_display_links = ['name']

    list_editable = ["status"]

    search_fields = ["name", "contact"]

    list_filter = ["status"]

    fieldsets = (
        ("Personal Info", {"fields": ("name", "date_of_birth", "father_name", "cnic")}),
        (
            "Contact Info",
            {
                "fields": ("address", "contact"),
            },
        ),
        (
            "Enrollment Info",
            {
                "fields": ["status"],
            },
        ),
    )


admin.site.register(Client, ClientAdmin)
