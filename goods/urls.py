from django.urls import path
from .views import CatalogView, CatalogCategoryView, FilteredProductsView, product_add, get_product_list

app_name = 'goods'

urlpatterns = [
    path('', CatalogView.as_view(),  name='catalog'),
    path('category/<slug:category_slug>', CatalogCategoryView.as_view(),  name='category'),
    path('filter/', FilteredProductsView.as_view(), name='filter'),
    path('add_to_store/', product_add, name='add_to_store'),
    path('prlst/', get_product_list, name='prlst'),
]