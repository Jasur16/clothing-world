from django import template

register = template.Library()
from shop.models import WishlistModel

@register.filter()
def is_wishlist(product, request):
    return WishlistModel.objects.filter(user=request.user, product=product).exists()
