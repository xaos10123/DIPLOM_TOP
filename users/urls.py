from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import *

app_name = "user"

urlpatterns = [
    path("login/", login_view, name="login"),
    path("register/", registration_view, name="register"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("logout/", LogoutView.as_view(next_page="main:index"), name="logout"),
    path("set-active-address/", set_active_address, name="set_active_address"),
    path("add-address/", add_address, name="add_address"),
    path("del_address/<int:adress_id>/", del_address, name="del_address"),
    path("users_cart/", users_cart, name="users_cart"),
    path('password_reset/', password_reset_view, name='password_reset'),
]
