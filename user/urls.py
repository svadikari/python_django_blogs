from django.contrib.auth import views as auth_view
from django.urls import path

from .views import create_user, profile

app_name = 'user'

urlpatterns = [
  path('user', create_user, name='register'),
  path('login/', auth_view.LoginView.as_view(template_name='user/login.html'),
       name='login'),
  path('logout/', auth_view.LogoutView.as_view(), name='logout'),
  path('profile/', profile, name='profile'),
]
