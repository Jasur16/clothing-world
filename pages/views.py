from django.shortcuts import render, reverse
from django.views.generic import TemplateView, CreateView, ListView
from blogs.models import PostModel
from shop.models import BarCategoryModel, CategoryModel, ProductModel, ProductTagModel, SizeModel, ColorModel
from .models import MenBannerModel, WomenBannerModel
from .forms import ContactModelForm


class HomeView(ListView):
    template_name = 'index.html'

    def get_queryset(self):
        qs = ProductModel.objects.all()

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

    def get_context_data(self, object_list=None, **kwargs):
        data = super().get_context_data(**kwargs)
        data['men_banners'] = MenBannerModel.objects.filter(is_active=True).order_by('-pk')
        data['categories'] = CategoryModel.objects.all()
        data['tags'] = ProductTagModel.objects.all()
        data['bar_categories'] = BarCategoryModel.objects.all()
        data['sizes'] = SizeModel.objects.all()
        data['colors'] = ColorModel.objects.all()
        data['products'] = ProductModel.objects.all()
        return data


class WomenView(TemplateView):
    template_name = 'women.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['posts'] = PostModel.objects.order_by('-pk')[:3]
        data['women_banners'] = WomenBannerModel.objects.filter(is_active=True).order_by('-pk')
        return data


class ContactView(CreateView):
    template_name = 'contact.html'
    form_class = ContactModelForm

    def get_success_url(self):
        return reverse('pages:contact')
