from django.shortcuts import render, redirect
from .models import UserModel
from .forms import RegistrationForm, LoginForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.generic import TemplateView


class MyAccount(TemplateView):
    template_name = 'my_account.html'


def users_login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])

        if not user is None:
            login(request, user)
            redirect('pages:home')
        else:
            form.add_error('password', 'Parol yoki Username no\'tog\'ri')

    return render(request, 'login.html', context={
        'form': form
    })


def user_registration(request):
    form = RegistrationForm
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            password = form.cleaned_data['password']
            user = User(
                username=username,
                first_name=first_name,
                last_name=last_name,
                password=make_password(password)
            )
            user.save()
            return redirect('pages:home')

    return render(request, 'registration.html', context={
        'form': form
    })
