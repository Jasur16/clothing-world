from django.shortcuts import render
from django.views.generic import CreateView
from .forms import CheckoutForm
from .models import ShopHistoryModel


class CheckoutView(CreateView):
    form_class = CheckoutForm
    template_name = 'checkout.html'
    model = ShopHistoryModel
