from django.urls import path

from .views import HomeView, BlogDetailView, BlogCreateView, delete

app_name = 'blog'

urlpatterns = [
  path('', HomeView.as_view(), name='home'),
  path('<int:pk>/', BlogDetailView.as_view(), name='detail'),
  path('create/', BlogCreateView.as_view(), name="create"),
  path('delete/<int:pk>', delete, name="delete"),
]
