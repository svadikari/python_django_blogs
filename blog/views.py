from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

import user
from .models import Blog


class HomeView(LoginRequiredMixin, ListView):
  model = Blog
  template_name = 'blog/home.html'
  context_object_name = 'blogs'
  paginate_by = 5

  def get_queryset(self, *args, **kwargs):
    username = self.request.GET.get('filterByUser')
    if username:
      user = get_object_or_404(User, username=username)
      self.extra_context = {'filterByUser': username}
      return Blog.objects.filter(author=user).order_by('-created_at')
    return Blog.objects.all().order_by('-created_at')


class BlogDetailView(LoginRequiredMixin, UpdateView):
  model = Blog
  template_name = 'blog/detail.html'
  context_object_name = 'form'
  fields = ['title', 'detail']
  success_url = '/'


class BlogCreateView(LoginRequiredMixin, CreateView):
  model = Blog
  template_name = 'blog/create.html'
  fields = ['title', 'detail']
  success_url = '/'

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)

@login_required
def delete(request, **kwargs):
  blog = Blog.objects.filter(id = kwargs.get('pk', int)).first()
  if blog:
    if user != blog.author:
      messages.error(request, "You are not allowed delete others blogs", extra_tags='danger')
    else:
      blog.delete()
      messages.success(request, "Blog deleted.")
  else:
    messages.error(request, "Blog not found.", extra_tags='danger')
  return redirect('/')

