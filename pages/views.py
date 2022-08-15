from django.shortcuts import render, reverse, redirect
from django.template.loader import render_to_string
from django.views.generic import TemplateView, CreateView, ListView
from blogs.models import PostModel
from shop.models import BarCategoryModel, CategoryModel, ProductModel, ProductTagModel, SizeModel, ColorModel
from .models import MenBannerModel, WomenBannerModel, AboutModel
from .forms import ContactForm
from django.core.mail import send_mail


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

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data()
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


class AboutView(ListView):
    model = AboutModel
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data()
        data['abouts'] = AboutModel.objects.all()
        return data


# class ContactView(CreateView):
#     template_name = 'contact.html'
#     form_class = ContactModelForm
#
#     def get_success_url(self):
#         return reverse('pages:contact')


def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data['phone'])
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']

            html = render_to_string('contactform.html',
                                    {'name': name, 'email': email, 'phone': phone, 'message': message})

            send_mail('The contact form subject', 'This is the message', 'user@codewithstein.com',
                      ['jasurisrailov1@gmail.com'], html_message=html)

            return redirect('pages:contact')
    else:
        form = ContactForm()

    return render(request, 'contact.html', context={
        'form': form,
    })


class ShoppingCart(TemplateView):
    template_name = 'shopping-cart.html'
