from django.db.models import Sum
from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, CreateView
import random
from orders.forms import CheckoutForm
from orders.models import OrderHistoryModel
from shop.models import ProductModel


class ShoppingCart(ListView):
    template_name = 'shopping-cart.html'

    def get_queryset(self):
        products = ProductModel.get_cart_objects(self.request)
        return products


class CheckoutView(CreateView):
    form_class = CheckoutForm
    model = OrderHistoryModel
    template_name = 'checkout.html'
    success_url = 'order/history/'

    def dispatch(self, request, *args, **kwargs):
        if len(request.session.get('cart', [])) == 0:
            return redirect(reverse('pages:home'))
        return super(CheckoutView, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('orders:history')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['products'] = ProductModel.get_cart_objects(self.request)
        context['orders'] = ProductModel.objects.filter(wishlistmodel__user_id=self.request.user)

        if hasattr(self.request.user, 'profiles'):
            context['profile'] = self.request.user.profiles

        return context

    def form_valid(self, form):
        products = ProductModel.get_cart_objects(self.request)
        price = products.aggregate(Sum('real_price')).get('real_price__sum', '')

        order = form.save(commit=True)

        if self.request.user.is_authenticated:
            order.user_id = self.request.user.id
        order.total_price = price
        order.products.set(products)
        order.save()

        self.request.session['cart'] = []
        return super().form_valid(form)


class OrderHistoryView(ListView):
    template_name = 'order-history.html'

    def get_queryset(self):
        return OrderHistoryModel.objects.filter(user=self.request.user.id)

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data()
        data['orders'] = ProductModel.objects.filter(wishlistmodel__user_id=self.request.user)
        return data
