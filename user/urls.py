from django.urls import path
from .views import MyAccountView, login_view, user_registration, logout_view, ProfileView

app_name = 'user'

urlpatterns = [
    path('my-account/', MyAccountView.as_view(), name='my-account'),
    path('login/', login_view, name='login'),
    path('registration/', user_registration, name='registration'),
    path('user/logout/', logout_view, name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
