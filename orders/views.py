from django.shortcuts import render, reverse, redirect
from django.views.generic import CreateView, TemplateView
from .forms import CheckoutForm
from .models import OrderHistoryModel
from shop.models import ProductModel
from user.models import ProfileModel


class OrderHistoryView(TemplateView):
    template_name = 'order-history.html'


class CheckoutView(CreateView):
    form_class = CheckoutForm
    template_name = 'checkout.html'
    model = OrderHistoryModel

    def dispatch(self, request, *args, **kwargs):
        if len(request.session.get('cart', [])) == 0:
            return redirect(reverse('pages:home'))
        return super(CheckoutView, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('orders:history')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['products'] = ProductModel.get_cart_objects(self.request)

        if hasattr(self.request.user, 'profiles'):
            context['profile'] = self.request.user.profiles

        return context
