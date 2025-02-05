from django.urls import path

from promotions.views import PromoListView, PromoDetailView

app_name = "promo"

urlpatterns = [
    path("list/", PromoListView.as_view(), name="promo_list"),
    path("<int:pk>/", PromoDetailView.as_view(), name="promo_detail"),
]
