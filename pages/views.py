from django.shortcuts import render, reverse
from django.views.generic import TemplateView, CreateView
from blogs.models import PostModel
from shop.models import BarCategoryModel, CategoryModel
from .models import MenBannerModel, WomenBannerModel
from .forms import ContactModelForm


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['men_banners'] = MenBannerModel.objects.filter(is_active=True).order_by('-pk')
        data['bar_categories'] = BarCategoryModel.objects.all()
        data['categories'] = CategoryModel.objects.all()
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
