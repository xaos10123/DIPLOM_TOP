from django.shortcuts import render
from django.views import View
from main.views import CustomHtmxMixin


class LoginView(CustomHtmxMixin, View):
    template_name = "users/login.html"
    def get(self, request):
        return render(request, "users/login.html")


class RegisterView(CustomHtmxMixin, View):
    template_name = "users/register.html"
    def get(self, request):
        return render(request, "users/register.html")


class ProfileView(CustomHtmxMixin, View):
    template_name = "users/profile.html"
    def get(self, request):
        return render(request, "users/profile.html")


def logout_view(request):
    return render(request, "users/logout.html")
