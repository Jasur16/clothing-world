from django.urls import path
from .views import CheckoutView, OrderHistoryView

app_name = 'orders'

urlpatterns = [
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('history/', OrderHistoryView.as_view(), name='history'),
]
