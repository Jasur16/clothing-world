from django.urls import path
from .views import PostView, PostDetailView, CommentCreateView

app_name = 'blogs'

urlpatterns = [
    path('', PostView.as_view(), name='posts'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('<int:pk>/comment/', CommentCreateView.as_view(), name='comment')
]
