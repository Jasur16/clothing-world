from django.core.validators import ValidationError
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.utils.translation import gettext_lazy as _


class MyAccountView(TemplateView):
    template_name = 'my_account.html'


def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(request, **form.cleaned_data)
            if user is not None:
                login(request, user)

                messages.success(request, _('добро пожаловать!'))
                return redirect('pages:home')

        form.add_error('password', _("Логин или пароль неверный"))

    return render(request, 'login.html', {
        'form': form
    })


# def login_view(request):
#     form = LoginForm
#     if request.method == 'POST':
#         form = LoginForm(data=request.POST)
#
#         if form.is_valid():
#             user = authenticate(
#                 username=form.cleaned_data['password'],
#                 password=form.cleaned_data['password']
#             )
#             if user is not None:
#                 login(request, user)
#                 return redirect('pages:home')
#             raise ValidationError('Имя пользователя или пароль неверный!')
#
#     return render(request, 'login.html', context={
#         'form': form,
#     })


def user_registration(request):
    form = RegistrationForm()

    if request.method == "POST":
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            del form.cleaned_data['confirm_password']
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()

            messages.success(request, _("Вы успешно зарегистрировались"))

            return redirect('user:login')

    return render(request, 'registration.html', context={
        'form': form
    })


def logout_view(request):
    messages.success(request, _('Приходите !'), request.user.get_full_name(), '!')
    logout(request)

    return redirect('pages:home')
