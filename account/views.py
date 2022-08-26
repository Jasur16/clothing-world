from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from .forms import RegistrationForm, LoginForm
from django.utils.translation import gettext_lazy as _


class MyAccountView(TemplateView):
    template_name = 'my_account.html'


def account_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(request, **form.cleaned_data)
            if user is not None:
                login(request, user)

                messages.success(request, _('добро пожаловать!'))
                return redirect('pages:home')

        form.add_error('password', _("Логин и/или пароль неверный"))

    return render(request, 'login.html', {
        'form': form
    })


def account_registration(request):
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.instance.set_password(form.cleaned_data.get('password'))
            form.save()

        messages.success(request, _("Вы успешно зарегистрировались"))

        return redirect('login')

    return render(request, 'registration.html', {
        'form': form
    })


# def account_registration(request):
#     form = RegistrationForm()
#     if request.method == 'POST':
#         form = RegistrationForm(data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             password = form.cleaned_data['password']
#             user = User(
#                 username=username,
#                 first_name=first_name,
#                 last_name=last_name,
#                 password=password
#             )
#             print(user)
#
#             # user.save()
#
#         messages.success(request, "Siz muvaffaqiyatli ro'yxatdan o'tdingiz")
#         return redirect('login')
#
#     return render(request, 'registration.html', {
#         'form': form
#     })


def account_logout(request):
    messages.success(request, _('Приходите !'), request.user.get_full_name(), '!')
    logout(request)

    return redirect('pages:home')
