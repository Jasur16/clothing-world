from django.urls import path
from .views import ShopView, ProductDetailView, wishlist_view, WishlistView, update_cart_view, ShoppingCartView, \
    checkout_cart

app_name = 'shop'

urlpatterns = [
    path('', ShopView.as_view(), name='home'),
    # path('posts-json/', PostJsonListModel.as_view(), name='posts-json'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='detail'),
    path('product/<int:pk>/wishlist_view', wishlist_view, name='wishlist'),
    path('wishlists/', WishlistView.as_view(), name='all_wishlist'),
    path('add_cart/<int:id>/', update_cart_view, name='cart'),
    path('checkout/', checkout_cart, name='checkout'),
    path('shopping-cart/', ShoppingCartView.as_view(), name='shopping-cart'),
]
