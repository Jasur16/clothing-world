from django.urls import path
from .views import HomeView, ContactView, WomenView, AboutView

app_name = 'pages'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('women/', WomenView.as_view(), name='women')
]
