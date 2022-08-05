from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import ProductModel


class ShopView(ListView):
    template_name = 'product.html'

    def get_queryset(self):
        qs = ProductModel.objects.order_by('-id')

        search = self.request.GET.get('search')
        if search:
            qs = qs.filter(title__icontains=search)
        return qs


class ProductDetailView(DetailView):
    model = ProductModel
    template_name = 'product-detail.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data()
        data['products'] = ProductModel.objects.all().exclude(id=self.object.pk)
        return data