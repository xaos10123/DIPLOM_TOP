from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import RegisterView, ProfileView, logout_view, login_view

app_name = 'user'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(next_page='main:index'), name='logout'),

    
]