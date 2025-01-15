from django.db.models import Q, Max, Min
from django.shortcuts import render, HttpResponse
from django.views.generic import ListView
from main.views import CustomHtmxMixin
from .models import Product, Categories


class CatalogView(CustomHtmxMixin, ListView):
    model = Product
    template_name = "goods/catalog.html"
    context_object_name = "goods"

    def get_context_data(self, **kwargs):
        kwargs["categories"] = Categories.objects.all()
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


def get_filtered_products(request):
    category_id = request.GET.get('category')
    query = Q()

    products = Product.objects.all()
    
    name = request.GET.get('name').title()
    category_id = request.GET.get('category')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    oreding = request.GET.get('oreding')
    sale = request.GET.get('sale')

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


    if products.exists():
        return render(request, 'goods/filtered_items.html', {'goods': products})
    
    return render(request, 'goods/not_found_item.html', {})
