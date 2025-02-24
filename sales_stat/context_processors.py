from django.core.cache import cache
from goods.models import Categories


def categories_processor(request):
    categories = cache.get("categories")
    if not categories:
        categories = Categories.objects.all()
    return {"categories": categories}
