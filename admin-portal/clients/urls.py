from django.urls import re_path
from . import views


urlpatterns = [re_path(r"^$", views.get_all_clients, name="get_all_clients")]
