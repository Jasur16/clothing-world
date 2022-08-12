from django.urls import path
from .views import MyAccountView, account_registration, account_login, account_logout

urlpatterns = [
    path('my-account/', MyAccountView.as_view(), name='my-account'),
    path('user/registration/', account_registration, name='registration'),
    path('user/login/', account_login, name='login'),
    path('user/logout/', account_logout, name='logout'),
]
