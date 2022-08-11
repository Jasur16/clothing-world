from django.urls import path
from .views import MyAccountView, account_registration

urlpatterns = [
    path('my-account/', MyAccountView.as_view(), name='my-account'),
    path('user/registration/', account_registration, name='registration')
]
