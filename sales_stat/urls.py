from django.urls import path
from .views import index, best_sales

app_name = "sales_stat"

urlpatterns = [
    path('', index, name='index'),
    path('best_sales/', best_sales, name='best_sales'),
]
