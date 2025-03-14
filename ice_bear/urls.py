"""
URL configuration for ice_bear project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path

from django.conf.urls.static import static
from ice_bear import settings


urlpatterns = [
    path('admin/dashboards/', include('dashboards.urls')),
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('catalog/', include('goods.urls')),
    path('user/', include('users.urls')),
    path('cart/', include('carts.urls')),
    path('orders/', include('orders.urls')),
    path('promo/', include('promotions.urls')),
    path('delivery_panel/', include('delivery_panel.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
