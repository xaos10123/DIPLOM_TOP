import json
from django.shortcuts import render
from django.db.models import Count
from django.db.models.functions import TruncDate
from orders.models import Order

from goods.models import Categories, Product


def index(request):
    category = Categories.objects.all()
    orders_by_day = Order.objects.filter(status='Доставлен').annotate(
    date=TruncDate('created_timestamp')
    ).values('date').annotate(
        count=Count('id')
    ).order_by('date')
    result = [{'date': item['date'].strftime('%d.%m'),'count': item['count']} for item in orders_by_day]

    data = {
        "base_count_items": {
            "labels": [category.name for category in category],
            "data": [category.products.count() for category in category],
            "type": "polarArea",
        },
        "base_count_orders": {
            "labels": [item["date"] for item in result],
            "data": [item["count"] for item in result],
            "type": "line",
        },
    }
    context = {
        "chartData": json.dumps(data),
    }
    return render(request, "sales_stat/index.html", context=context)


def best_sales(request):
    qset = Product.objects.all().order_by('-order_amount')[:10]
    data = {
        "labels": [f'{item.name} {item.char}' for item in qset],
        "data": [item.order_amount for item in qset],
    }
    context = {
        "chartData": json.dumps(data),
        "type": "bar",
    }
    return render(request, "sales_stat/best_sales.html", context=context)

def rem_goods(request, category_slug):
    qset = Product.objects.filter(category__slug=category_slug).order_by('-quantity')
    data = {
        "labels": [f'{item.name} {item.char}' for item in qset],
        "data": [item.quantity for item in qset],
    }
    context = {
        
        "chartData": json.dumps(data),
        "type": "bar",
    }
    return render(request, "sales_stat/rem_goods.html", context=context)
