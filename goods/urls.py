from django.urls import path
from .views import catalog

app_name = 'goods'

urlpatterns = [
    path('', catalog,  name='catalog'),
]