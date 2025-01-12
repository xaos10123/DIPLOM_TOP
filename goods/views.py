from django.shortcuts import render
from .models import Product

def catalog(request):
    goods = Product.objects.all()
    
    context= {
        'title': 'Каталог',
        'goods': goods,
    }
    return render(request, 'goods/catalog.html', context=context)
