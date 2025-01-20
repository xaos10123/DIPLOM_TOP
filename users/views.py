from django.contrib import auth
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from main.views import CustomHtmxMixin
from users.forms import UserLoginForm, UserRegistrationForm


def login_view(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return render(
                request,
                "users/success_login.html",
                {
                    "title_block": "Вы успешно вошли в систему!",
                    "link_to": reverse_lazy("goods:catalog"),
                    "link_to_text": "Перейти к покупкам",
                },
            )
    else:
        form = UserLoginForm()
    return render(request, "users/login.html", {"form": form})


def registration_view(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            return render(
                request,
                "users/success_login.html",
                {
                    "title_block": "Регистрация прошла успешно!",
                    "link_to": reverse_lazy("goods:catalog"),
                    "link_to_text": "Перейти к покупкам",
                }
            )
    else:
        form = UserRegistrationForm()
    return render(request, "users/register.html", {"form": form})


class ProfileView(CustomHtmxMixin, View):
    template_name = "users/profile.html"

    def get(self, request):
        return render(request, "users/profile.html")


def logout_view(request):
    return render(request, "users/logout.html")
