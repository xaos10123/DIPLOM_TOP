from django.urls import path
from .views import CatalogView, CatalogCategoryView, get_filtered_products

app_name = 'goods'

urlpatterns = [
    path('', CatalogView.as_view(),  name='catalog'),
    path('category/<slug:category_slug>', CatalogCategoryView.as_view(),  name='category'),
    path('filter/', get_filtered_products, name='filter'),
]