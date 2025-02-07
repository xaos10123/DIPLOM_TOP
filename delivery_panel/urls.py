from django.urls import path

from delivery_panel.views import list_delivery

app_name = "delivery"

urlpatterns = [
    path("", list_delivery, name="delivery_panel"),
]
