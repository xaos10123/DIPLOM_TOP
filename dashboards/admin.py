from django.contrib import admin
from goods.models import Product
from orders.models import Order


class CustomIndexDashboard:
    def __init__(self, context):
        self.context = context
        self.children = []

    def init_with_context(self, context):
        # Добавляем блоки на дашборд
        self.children.append(
            {
                "type": "title",
                "title": "Управление магазином",
            }
        )

        # Блок статистики
        self.children.append(
            {
                "type": "stats",
                "models": [
                    {
                        "label": "Товары",
                        "count": Product.objects.count(),
                        "url": "admin:goods_product_changelist",
                    },
                    {
                        "label": "Заказы",
                        "count": Order.objects.count(),
                        "url": "admin:orders_order_changelist",
                    },
                ],
            }
        )

        # Блок быстрых действий
        self.children.append(
            {
                "type": "quick_actions",
                "entries": [
                    {
                        "title": "Добавить товар",
                        "url": "admin:goods_product_add",
                    },
                    {
                        "title": "Просмотр заказов",
                        "url": "admin:orders_order_changelist",
                    },
                ],
            }
        )
