from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.models import User


class MyAccountView(TemplateView):
    template_name = 'my_account.html'


def account_registration(request):
    if request.method == 'POST':
        # user = User(
        #     first_name=request.POST.get('first'),
        #     last_name=request.POST.get('last'),
        #     username=request.POST.get('username'),
        #     password=request.POST.get('password'),
        # )
        # user.set_password(request.POST.get('password'))
        # user.save()

        messages.success(request, "Siz muvaffaqiyatli ro'yxatdan o'tdingiz")

        return redirect('pages:home')

    return render(request, 'registration.html')
