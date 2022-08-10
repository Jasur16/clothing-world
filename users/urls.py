from django.urls import path
from .views import user_registration, users_login, MyAccount

urlpatterns = [
    path('user/registration/', user_registration, name='registration'),
    path('user/login/', users_login, name='login'),
    path('user/my_account/', MyAccount.as_view(), name='my_account')
]
