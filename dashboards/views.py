import json
from django.db import models
from django.shortcuts import render
from django.db.models import Count, Sum, Avg
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models.functions import TruncDate
from orders.models import Order
from goods.models import Categories, Product
from datetime import date
from django.db.models import Sum, Count
from django.utils import timezone
from datetime import datetime, time

from users.models import User


def get_summary_stats():
    today = timezone.now().date()
    today_start = timezone.make_aware(datetime.combine(today, time.min))
    today_end = timezone.make_aware(datetime.combine(today, time.max))

    return {
        "couriers_count": User.objects.filter(
            models.Q(delivery_orders__isnull=False) | models.Q(groups__name="Курьер")
        )
        .distinct()
        .count(),
        "products_count": Product.objects.count(),
        "total_revenue": Order.objects.filter(status="Доставлен").aggregate(
            total=Sum("items__price")
        )["total"]
        or 0,
        "today_revenue": Order.objects.filter(
            status="Доставлен", created_timestamp__range=(today_start, today_end)
        ).aggregate(total=Sum("items__price"))["total"]
        or 0,
        "today_orders": Order.objects.filter(
            created_timestamp__range=(today_start, today_end)
        ).count(),
    }

def get_discount_stats():
    discounted_products = Product.objects.filter(discaunt__gt=0)
    discount_stats = []
    
    for product in discounted_products:
        original_revenue = product.price * product.order_amount
        discounted_revenue = product.sell_price() * product.order_amount
        discount_cost = original_revenue - discounted_revenue
        
        if discount_cost > 0:
            roi = ((discounted_revenue - discount_cost) / discount_cost) * 100
        else:
            roi = 0
            
        discount_stats.append({
            'name': f"{product.name} {product.char}",
            'discount': product.discaunt,
            'orders': product.order_amount,
            'roi': round(roi, 2)
        })
    
    return sorted(discount_stats, key=lambda x: x['roi'], reverse=True)


def get_category_stats():
    return Categories.objects.all()


def get_top_products():
    return Product.objects.all().order_by("-order_amount")[:10]


def get_orders_by_day():
    return (
        Order.objects.filter(status="Доставлен")
        .annotate(date=TruncDate("created_timestamp"))
        .values("date")
        .annotate(count=Count("id"))
        .order_by("date")
    )


def get_average_check():
    return (
        Order.objects.filter(status="Доставлен")
        .annotate(date=TruncDate("created_timestamp"))
        .values("date")
        .annotate(avg_amount=Avg("items__price"))
        .order_by("date")
    )


def get_user_average():
    return (
        Order.objects.filter(status="Доставлен")
        .values("user__username")
        .annotate(avg_sum=Avg("items__price"))
        .order_by("-avg_sum")[:10]
    )


def get_courier_stats():
    return (
        Order.objects.filter(status="Доставлен")
        .values("delivery_man__username")
        .annotate(orders_count=Count("id"))
        .exclude(delivery_man__username=None)
        .order_by("-orders_count")
    )


def get_revenue_stats():
    return (
        Order.objects.filter(status="Доставлен")
        .annotate(date=TruncDate("created_timestamp"))
        .values("date")
        .annotate(total_revenue=Sum("items__price"))
        .order_by("date")
    )


def get_stock_levels():
    return Product.objects.values("id", "name", "char", "quantity").order_by(
        "-quantity"
    )


@staff_member_required
def dashboard(request):
    category = get_category_stats()
    qset = get_top_products()
    orders_by_day = get_orders_by_day()
    avg_order_amounts = get_average_check()
    avg_user_orders = get_user_average()
    courier_efficiency = get_courier_stats()
    revenue_by_day = get_revenue_stats()
    summary_stats = get_summary_stats()
    stock_items = Product.objects.all().order_by("quantity")
    stock_levels = get_stock_levels()
    discount_stats = get_discount_stats()

    result = [
        {"date": item["date"].strftime("%d.%m"), "count": item["count"]}
        for item in orders_by_day
    ]

    avg_result = [
        {"date": item["date"].strftime("%d.%m"), "avg": round(item["avg_amount"], 2)}
        for item in avg_order_amounts
    ]

    user_order_result = [
        {
            "username": item["user__username"] or "Гость",
            "avg": round(item["avg_sum"], 2),
        }
        for item in avg_user_orders
    ]

    courier_result = [
        {"courier": item["delivery_man__username"], "count": item["orders_count"]}
        for item in courier_efficiency
    ]

    revenue_result = [
        {"date": item["date"].strftime("%d.%m"), "revenue": item["total_revenue"]}
        for item in revenue_by_day
    ]

    stock_result = [
        {
            "product": f"{item['name']} {item['char']}",
            "quantity": item["quantity"],
            "id": item["id"],
        }
        for item in stock_levels
    ]

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
        "category_sale": {
            "labels": [f"{item.name} {item.char}" for item in qset],
            "data": [item.order_amount for item in qset],
            "type": "bar",
        },
        "average_check": {
            "labels": [item["date"] for item in avg_result],
            "data": [item["avg"] for item in avg_result],
            "type": "line",
        },
        "user_average": {
            "labels": [item["username"] for item in user_order_result],
            "data": [item["avg"] for item in user_order_result],
            "type": "bar",
        },
        "courier_stats": {
            "labels": [item["courier"] for item in courier_result],
            "data": [item["count"] for item in courier_result],
            "type": "bar",
        },
        "total_revenue": {
            "labels": [item["date"] for item in revenue_result],
            "data": [item["revenue"] for item in revenue_result],
            "type": "line",
        },
        "stock_levels": {
            "labels": [item["product"] for item in stock_result],
            "data": [item["quantity"] for item in stock_result],
            "ids": [item["id"] for item in stock_result],
            "type": "bar",
        },
        "discount_stats": {
        'labels': [item['name'] for item in discount_stats],
        'data': [item['roi'] for item in discount_stats],
        'discounts': [item['discount'] for item in discount_stats],
        'orders': [item['orders'] for item in discount_stats],
        'type': 'bar'
        },
    }

    return render(
        request,
        "dashboards/dasboards.html",
        {
            "chartData": json.dumps(data),
            "summary": summary_stats,
            "stock_items": stock_items,
            "today": date.today(),
        },
    )
