from django.db.models import Sum
from django.shortcuts import render, reverse, redirect
from django.views.generic import CreateView, TemplateView, ListView
from .forms import CheckoutForm
from .models import OrderHistoryModel
from shop.models import ProductModel
from user.models import ProfileModel


class CheckoutView(CreateView):
    form_class = CheckoutForm
    template_name = 'checkout.html'
    model = OrderHistoryModel
    success_url = 'history/'

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

    def dispatch(self, request, *args, **kwargs):
        if len(request.session.get('cart', [])) == 0:
            return redirect(reverse('pages:home'))
        return super(CheckoutView, self).dispatch(request, *args, **kwargs)
