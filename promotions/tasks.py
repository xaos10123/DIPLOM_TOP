from django.utils import timezone
from .models import Promo

def check_expired_promos():
    today = timezone.now().date()
    expired_promos = Promo.objects.filter(promo_end_date__lt=today, promo_status=True)
    
    for promo in expired_promos:
        products = promo.promo_products.all()
        
        for product in products:
            active_promos = product.promo_set.filter(
                promo_end_date__gte=today,
                promo_status=True
            ).exclude(id=promo.id)
            
            if active_promos.exists():
                max_discount = max(active_promos.values_list('promo_discount', flat=True))
                product.discaunt = int(max_discount)
            else:
                product.discaunt = 0
            product.save()
        
        promo.promo_status = False
        promo.save()
