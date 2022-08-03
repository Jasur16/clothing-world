from django.shortcuts import render
from django.views.generic import TemplateView


class ShopView(TemplateView):
    template_name = 'product.html'
