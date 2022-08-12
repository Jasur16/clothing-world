from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from .forms import RegistrationForm, LoginForm


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

                messages.success(request, f"{user.get_full_name()} xush kelibsiz!")
                return redirect('pages:home')

        form.add_error('password', "Login va/yoki parol no'tog'ri")

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

        messages.success(request, "Siz muvaffaqiyatli ro'yxatdan o'tdingiz")

        return redirect('login')

    return render(request, 'registration.html', {
        'form': form
    })


def account_logout(request):
    messages.success(request, f"Kelib turing {request.user.get_full_name()}!")
    logout(request)

    return redirect('pages:home')
