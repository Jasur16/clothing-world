from django.shortcuts import render
from django.views.generic import ListView
from .models import ProductModel


class ShopView(ListView):
    template_name = 'product.html'

    def get_queryset(self):
        return ProductModel.objects.order_by('-id')

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     data = super().get_context_data(**kwargs)
    #     data['products'] = ProductModel.objects.filter()
    #     return data
