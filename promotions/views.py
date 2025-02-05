from django.views.generic import DetailView, ListView

from promotions.models import Promo


class PromoListView(ListView):
    model = Promo
    template_name = "promotions/promo_list.html"
    context_object_name = "promos"

    def get_queryset(self):
        return Promo.objects.filter(promo_status=True)
    
class PromoDetailView(DetailView):
    model = Promo
    template_name = "promotions/promo_detail.html"
    context_object_name = "promo"