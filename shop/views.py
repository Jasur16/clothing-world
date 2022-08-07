from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from .models import ProductModel, CategoryModel, ProductTagModel, BarCategoryModel, ColorModel, SizeModel, \
    ProductDetailImageModel, WishlistModel


class ShopView(ListView):
    template_name = 'product.html'

    def get_queryset(self):
        qs = ProductModel.objects.all()

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
        return data


class ProductDetailView(DetailView):
    model = ProductModel
    template_name = 'product-detail.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data()
        data['products'] = ProductModel.objects.all().exclude(id=self.object.pk)
        data['sizes'] = SizeModel.objects.all()
        data['colors'] = ColorModel.objects.all()
        data['detail_images'] = ProductDetailImageModel.objects.all()
        return data


def wishlist_view(request, pk):
    product = get_object_or_404(ProductModel, pk=pk)
    WishlistModel.create_or_delete(request.user, product)
    return redirect(request.GET.get('next', '/'))
