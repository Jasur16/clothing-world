from django.urls import path
from .views import HomeView, ContactView, WomenView

app_name = 'pages'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('women/', WomenView.as_view(), name='women')
]
