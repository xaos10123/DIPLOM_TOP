from django.contrib import auth
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from main.views import CustomHtmxMixin
from users.forms import UserLoginForm

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)

            return HttpResponseRedirect(reverse_lazy('goods:catalog'))
    else:
        form = UserLoginForm()
    return render(request, 'users/login.html', {'form': form})

    


# class UserLoginView(CustomHtmxMixin, LoginView):
#     template_name = "users/login.html"
#     form_class = UserLoginForm   
#     success_url = reverse_lazy('goods:catalog')

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['form'] = self.form_class
#         return context

    
#     def form_valid(self, form):
#         user = form.get_user()

#         print(user)
#         return HttpResponseRedirect(self.get_success_url())




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
