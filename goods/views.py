from django.db.models import Q, Max, Min
from django.shortcuts import render
from django.views.generic import ListView
from main.views import CustomHtmxMixin
from .models import Product, Categories
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class CatalogView(CustomHtmxMixin, ListView):
    model = Product
    template_name = "goods/catalog.html"
    context_object_name = "goods"
    paginate_by = 12

    def get_context_data(self, **kwargs):
        kwargs["categories"] = Categories.objects.all()
        kwargs["all_items_count"] = Product.objects.count()
        price_stats = Product.objects.aggregate(max_price=Max('price'), min_price=Min('price'))
        kwargs["price_stats"] = price_stats
        return super().get_context_data(**kwargs)


class CatalogCategoryView(CustomHtmxMixin, ListView):
    model = Product
    template_name = "goods/catalog.html"
    context_object_name = "goods"

    def get_queryset(self):
        category_slug = self.kwargs.get("category_slug")
        return Product.objects.filter(category__slug=category_slug)
    
    def get_context_data(self, **kwargs):
        kwargs["categories"] = Categories.objects.all()
        price_stats = Product.objects.aggregate(max_price=Max('price'), min_price=Min('price'))
        kwargs["price_stats"] = price_stats
        kwargs["category_slug"] = self.kwargs.get("category_slug")
        return super().get_context_data(**kwargs)
    

class FilteredProductsView(ListView):
    model = Product
    template_name = "goods/filtered_items.html"
    context_object_name = "goods"
    paginate_by = 12

    def get_queryset(self):
        self.template_name = "goods/filtered_items.html"
        query = Q()

        products = Product.objects.all()

        name = self.request.GET.get('name')
        category_id = self.request.GET.get('category')
        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')
        oreding = self.request.GET.get('oreding')
        sale = self.request.GET.get('sale')

        if name:
            for word in name.split():
                query |= Q(name__icontains=word) | Q(char__icontains=word)
        if category_id:
            query &= Q(category_id=category_id)
        if min_price:
            query &= Q(price__gte=int(min_price))
        if max_price:
            query &= Q(price__lte=int(max_price))
        if sale == 'sale':
            query &= Q(discaunt__gt=0)

        products = products.filter(query)

        if oreding:
            if oreding == 'price_asc':
                products = products.order_by('price')
            elif oreding == 'price_desc':
                products = products.order_by('-price')


        if len(products)<1:
            self.template_name = 'goods/not_found_item.html'     
  
        return products
