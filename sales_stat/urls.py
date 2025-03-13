from django.urls import path
from .views import index, best_sales, rem_goods

app_name = "sales_stat"

urlpatterns = [
    path('', index, name='index'),
    path('best_sales/', best_sales, name='best_sales'),
    path('rem_goods/<slug:category_slug>', rem_goods, name='rem_goods'),
]
