from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Model
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, View, TemplateView, CreateView
from .models import ProductModel, CategoryModel, ProductTagModel, BarCategoryModel, ColorModel, SizeModel, \
    ProductDetailImageModel, WishlistModel


class ShopView(ListView):
    template_name = 'product.html'
    paginate_by = 12

    def get_queryset(self):
        qs = ProductModel.objects.filter()

        search = self.request.GET.get('search')
        if search:
            qs = qs.filter(title__icontains=search)

        cat = self.request.GET.get('cat')
        if cat:
            qs = qs.filter(category_id=cat)

        tag = self.request.GET.get('tag')
        if tag:
            qs = qs.filter(tags=tag)

        bar = self.request.GET.get('bar')
        if bar:
            qs = qs.filter(bar_category_id=bar)

        color = self.request.GET.get('color')
        if color:
            qs = qs.filter(colors=color)

        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data()
        data['categories'] = CategoryModel.objects.all()
        data['tags'] = ProductTagModel.objects.all()
        data['bar_categories'] = BarCategoryModel.objects.all()
        data['sizes'] = SizeModel.objects.all()
        data['colors'] = ColorModel.objects.all()
        data['products'] = ProductModel.objects.all()
        data['cart_product'] = ProductModel.get_cart_objects(self.request)
        data['model_image'] = ProductDetailImageModel.objects.all()
        data['product_modal'] = ProductModel.objects.all()
        return data


# class MainView(TemplateView):
#     template_name = 'posts-json.html'
#
#
# class PostJsonListModel(View):
#
#     def get(self, *args, **kwargs):
#         posts = list(ProductModel.objects.values())
#         return JsonResponse({'data': posts}, safe=False)


class ProductDetailView(DetailView):
    model = ProductModel
    template_name = 'product-detail.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data()
        data['products'] = ProductModel.objects.all().exclude(id=self.object.pk)
        # data['sizes'] = SizeModel.objects.all()
        # data['colors'] = ColorModel.objects.all()
        data['detail_images'] = ProductDetailImageModel.objects.all().filter(id=self.object.pk)
        data['cart_product'] = ProductModel.get_cart_objects(self.request)
        return data


@login_required
def wishlist_view(request, pk):
    product = get_object_or_404(ProductModel, pk=pk)
    WishlistModel.create_or_delete(request.user, product)
    return redirect(request.GET.get('next', '/'))


class WishlistView(LoginRequiredMixin, ListView):
    template_name = 'wishlist.html'

    def get_queryset(self):
        return ProductModel.objects.filter(wishlistmodel__user_id=self.request.user)

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data()
        data['orders'] = ProductModel.objects.filter(wishlistmodel__user_id=self.request.user)
        data['cart_product'] = ProductModel.get_cart_objects(self.request)
        return data


def update_cart_view(request, id):
    cart = request.session.get('cart', [])
    print(request.session.get('cart', []))

    if id in cart:
        cart.remove(id)
    else:
        cart.append(id)

    request.session['cart'] = cart
    return redirect(request.GET.get('next', '/'))


class ShoppingCartView(ListView):
    template_name = 'shopping-cart.html'

    def get_queryset(self):
        products = ProductModel.get_cart_objects(self.request)
        return products

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data()
        data['cart_product'] = ProductModel.get_cart_objects(self.request)
        return data


# class CheckoutView(CreateView):
#     form_class = CheckoutForm
#     template_name = 'checkout.html'
#     model = ShopHistoryModel

# def checkout_cart(request):
#     form = CheckoutForm()
#
#     return render(request, 'checkout.html', context={
#         'form': form,
#     })

# def shop_cart(request):
#     form = CheckoutForm()
#
#     return render(request, 'shopping-cart.html', context={
#         'form': form
#     })
