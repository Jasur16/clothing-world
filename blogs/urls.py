from django.urls import path
from .views import PostView, PostDetailView

app_name = 'blogs'

urlpatterns = [
    path('', PostView.as_view(), name='posts'),
]
