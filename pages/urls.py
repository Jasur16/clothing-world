from django.urls import path
from .views import HomeView, WomenView, AboutView, ShoppingCart, index

app_name = 'pages'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('shopping-cart/', ShoppingCart.as_view(), name='cart'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', index, name='contact'),
    path('women/', WomenView.as_view(), name='women')
]
