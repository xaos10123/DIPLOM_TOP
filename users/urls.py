from django.urls import path
from .views import LoginView, RegisterView, ProfileView, logout_view

app_name = 'user'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('logout/', logout_view, name='logout'),

    
]