from django.urls import path
from .views import CatalogView, CatalogCategoryView, FilteredProductsView

app_name = 'goods'

urlpatterns = [
    path('', CatalogView.as_view(),  name='catalog'),
    path('category/<slug:category_slug>', CatalogCategoryView.as_view(),  name='category'),
    path('filter/', FilteredProductsView.as_view(), name='filter'),
]