from django.urls import path

from .views import ShoppingCart, CheckoutView, OrderHistoryView

app_name = 'orders'

urlpatterns = [
    path('shopping-cart/', ShoppingCart.as_view(), name='cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('history/', OrderHistoryView.as_view(), name='history'),
]
