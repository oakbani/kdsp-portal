from django.contrib import admin

# Register your models here.

from .models import WaitingListOT, WaitingListPT, WaitingListST, MasterList


class WaitingListOTAdmin(admin.ModelAdmin):
    list_display = ["client", "date", "status"]
    list_editable = ["status"]
    pass


admin.site.register(WaitingListOT, WaitingListOTAdmin)


class WaitingListPTAdmin(admin.ModelAdmin):
    list_display = ["client", "date", "status"]
    pass


admin.site.register(WaitingListPT, WaitingListPTAdmin)


class WaitingListSTAdmin(admin.ModelAdmin):
    list_display = ["client", "date", "status"]
    pass


admin.site.register(WaitingListST, WaitingListSTAdmin)


class MasterListAdmin(admin.ModelAdmin):
    list_display = ["client", "date", "status"]
    pass


admin.site.register(MasterList, MasterListAdmin)
