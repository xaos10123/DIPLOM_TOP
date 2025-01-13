from django.views.generic import ListView
from main.views import CustomHtmxMixin
from .models import Product


class CatalogView(CustomHtmxMixin, ListView):
    model = Product
    template_name = "goods/catalog.html"
    context_object_name = "goods"

class CatalogCategoryView(CustomHtmxMixin, ListView):
    model = Product
    template_name = "goods/catalog.html"
    context_object_name = "goods"

    def get_queryset(self):
        category_slug = self.kwargs.get("category_slug")
        return Product.objects.filter(category__slug=category_slug)

