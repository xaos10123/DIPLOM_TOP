from django.db.models import Q, Max, Min
from django.views.generic import ListView, TemplateView
from main.views import CustomHtmxMixin
from .models import Product, Categories


class CatalogView(CustomHtmxMixin, TemplateView):
    model = Product
    template_name = "goods/catalog.html"    

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

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["name"] = self.request.GET.get('name')
        context["category"] = self.request.GET.get('category')
        context["min_price"] = self.request.GET.get('min_price')
        context["max_price"] = self.request.GET.get('max_price')
        context["oreding"] = self.request.GET.get('oreding')
        context["sale"] = self.request.GET.get('sale')
        return context

    def get_queryset(self):
        self.template_name = "goods/filtered_items.html"
        products = Product.objects.none()
        
        name = self.request.GET.get('name')
        category_id = self.request.GET.get('category')
        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')
        oreding = self.request.GET.get('oreding')
        sale = self.request.GET.get('sale')
        print(name, category_id, min_price, max_price, oreding, sale)

        products = Product.objects.all()
        
        if category_id:
            products = products.filter(category_id=category_id)
        if min_price:
            products = products.filter(price__gte=int(min_price))
        if max_price:
            products = products.filter(price__lte=int(max_price))
        if sale == 'sale':
            products = products.filter(discaunt__gt=0)
        if name:
            name_terms = name.split()
            name_query = Q()
            for term in name_terms:
                name_query |= Q(name__icontains=term) | Q(char__icontains=term)
            products = products.filter(name_query)

        if oreding:
            if oreding == 'price_asc':
                products = products.order_by('price')
            elif oreding == 'price_desc':
                products = products.order_by('-price')

        if not products.exists():
            self.template_name = 'goods/not_found_item.html'     

        return products.distinct()
    
    
