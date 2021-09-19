from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r"^therapists/$", views.get_all_therapists, name="get_all_therapists"),
    re_path(r"^slot/therapistid$", views.get_therapist_slot, name="get_therapist_slot"),
    re_path(r"^slot/add$", views.add_therapist_slot, name="add_therapist_slot"),
    re_path(
        r"^slot/update$", views.update_therapist_slot, name="update_therapist_slot"
    ),
    re_path(
        r"^slot/delete$", views.delete_therapist_slot, name="delete_therapist_slot"
    ),
]
