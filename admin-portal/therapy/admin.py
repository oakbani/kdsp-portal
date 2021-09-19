from django.contrib import admin

# Register your models here.

from .models import Therapist, TherapistSchedule, TherapyCenter, TherapySlot


class TherapistAdmin(admin.ModelAdmin):
    list_display = ["name", "OT", "PT", "ST"]
    search_fields = ["name", "contact"]
    fieldsets = (
        ("Personal and Contact Info", {"fields": ("name", "contact")}),
        (
            "Specialization",
            {
                "fields": ("OT", "PT", "ST"),
            },
        ),
    )


admin.site.register(Therapist, TherapistAdmin)


class TherapistScheduleAdmin(admin.ModelAdmin):
    list_display = ["therapist", "day", "start_time", "end_time", "therapy_center"]

    # search_fields = ['name']
    list_filter = ["day", "therapist__name", "therapy_center__title"]

    pass


admin.site.register(TherapistSchedule, TherapistScheduleAdmin)


class TherapyCenterAdmin(admin.ModelAdmin):
    list_display = ["title", "phone_no"]


admin.site.register(TherapyCenter, TherapyCenterAdmin)


class TherapySlotAdmin(admin.ModelAdmin):
    list_display = ["therapist", "client", "date", "start_time", "end_time", "status"]

    list_filter = ["date", "therapist__name", "client__name", "status"]

    fieldsets = (
        ("General Info", {"fields": ("title", "date", "start_time", "end_time")}),
        (
            "Therapist & Client",
            {
                "fields": ("therapist", "therapy_type", "client"),
            },
        ),
        (
            "Status",
            {
                "fields": ["status"],
            },
        ),
    )


admin.site.register(TherapySlot, TherapySlotAdmin)
