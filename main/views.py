from django.views.generic import ListView
from goods.models import Categories, Product


class CustomHtmxMixin:
    def dispatch(self, request, *args, **kwargs):
        # import pdb; pdb.set_trace()
        self.template_htmx = self.template_name
        if not self.request.META.get("HTTP_HX_REQUEST"):
            self.template_name = "include_block.html"

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        kwargs["template_htmx"] = self.template_htmx
        return super().get_context_data(**kwargs)


class IndexView(CustomHtmxMixin, ListView):
    model = Categories
    template_name = "main/index.html"
    context_object_name = "categories"

    def get_context_data(self, **kwargs):
        kwargs["title"] = 'Главная страница'
        kwargs["items_bests"] = Product.objects.order_by('-order_amount')[:10]

        return super().get_context_data(**kwargs)
