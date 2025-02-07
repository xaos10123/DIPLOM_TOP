from django.contrib import admin

from orders.models import Order, OrderItem


class OrderItemTabAdmin(admin.TabularInline):
    model = OrderItem
    fields = (
        "product",
        "quantity",
    )
    search_fields = ("product__name",)
    extra = 1


class OrderTabAdmin(admin.TabularInline):
    model = Order
    fields = (
        "user",
        "is_paid",
        "status",
    )
    search_fields = ("user__username",)
    extra = 1
    fk_name="user"


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "status",
        "created_timestamp",
    )
    list_filter = (
        "user",
        "status",
        "created_timestamp",
    )
    search_fields = ("user__username",)
    ordering = ("-created_timestamp",)
    readonly_fields = ("created_timestamp",)
    fk_name="user"

    inlines = [
        OrderItemTabAdmin,
    ]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = (
        "order",
        "product",
        "quantity",
    )
    list_filter = (
        "order",
        "product",
    )
    search_fields = ("product__name",)
