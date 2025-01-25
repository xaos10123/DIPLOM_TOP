from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from carts.models import Cart
from main.views import CustomHtmxMixin
from users.forms import UserLoginForm, UserRegistrationForm
from django.views.decorators.http import require_POST

from users.models import Adress


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
                },
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


def users_cart(request):
    carts = Cart.objects.filter(user=request.user).order_by('product__name', 'product__char')
    print(carts)
    return render(request, "users/users_cart.html", {"carts": carts})



@require_POST
@login_required
def set_active_address(request):
    address_id = request.POST.get("address_id")
    request.user.addresses.all().update(is_active=False)
    address = request.user.addresses.get(id=address_id)
    address.is_active = True
    address.save()
    request.session["active_address_id"] = address_id

    return render(request, "users/address_dropdown.html", {"active_address": address})


@login_required
def add_address(request):
    if request.method == "POST":
        city = request.POST.get("city")
        street = request.POST.get("street")
        house = request.POST.get("house")
        apartment = request.POST.get("apartment")

        request.user.addresses.all().update(is_active=False)

        Adress.objects.create(
            user=request.user,
            city=city,
            street=street,
            house=house,
            apartment=apartment,
            is_active=True,
        )
        return redirect("main:index")

    return render(request, "users/add_address.html")
