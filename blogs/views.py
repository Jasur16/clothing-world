from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import ListView, DetailView, CreateView
from .models import PostModel
from .forms import CommentModelForm
from shop.views import CategoryModel, ProductModel, ProductTagModel
from shop.models import ProductModel, BarCategoryModel


class PostView(ListView):
    queryset = PostModel.objects.order_by('-id')
    template_name = 'blog.html'
    paginate_by = 2

    def get_queryset(self):
        qs = PostModel.objects.filter()

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
        data['bar_categories'] = BarCategoryModel.objects.all()
        data['cart_product'] = ProductModel.get_cart_objects(self.request)
        return data


class PostDetailView(DetailView):
    model = PostModel
    template_name = 'blog-detail.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data()
        data['categories'] = CategoryModel.objects.all()
        data['products'] = ProductModel.objects.all()
        data['tags'] = ProductTagModel.objects.all()
        data['cart_product'] = ProductModel.get_cart_objects(self.request)
        return data


class CommentCreateView(CreateView):
    form_class = CommentModelForm

    def form_valid(self, form):
        form.instance.post = get_object_or_404(PostModel, pk=self.kwargs.get('pk'))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blogs:detail', kwargs={'pk': self.kwargs.get('pk')})
