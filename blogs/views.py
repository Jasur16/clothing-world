from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import ListView, DetailView, CreateView
from .models import PostModel
from .forms import CommentModelForm


class PostView(ListView):
    queryset = PostModel.objects.order_by('-id')
    template_name = 'blog.html'
    paginate_by = 2

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     data = super().get_context_data(**kwargs)
    #     data['posts'] = PostModel.object.all()
    #     return data


class PostDetailView(DetailView):
    model = PostModel
    template_name = 'blog-detail.html'


class CommentCreateView(CreateView):
    form_class = CommentModelForm

    def form_valid(self, form):
        form.instance.post = get_object_or_404(PostModel, pk=self.kwargs.get('pk'))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blogs:detail', kwargs={'pk': self.kwargs.get('pk')})

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['comments'] = CommentModelForm.object.all()