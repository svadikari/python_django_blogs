import os.path
import uuid
from os.path import splitext

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect, get_object_or_404

from user.forms import UserRegistrationForm, ProfileForm
from user.models import Profile


def create_user(request):
  if request.method == 'POST':
    form = UserRegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request,
                       f'Successfully  created {form.cleaned_data.get("username")}')
      return redirect('user:login')
  else:
    form = UserRegistrationForm()
  return render(request, 'user/register_user.html', {'form': form})


def save_image(image):
  _, ext = splitext(image.name)
  f_name = str( uuid.uuid4()) + ext
  fs = FileSystemStorage()
  fs.save(f_name, image)
  return f_name


@login_required
def profile(request):
  if request.method == 'POST':
    form = ProfileForm(request.POST, request.FILES)
    if form.is_valid():
      user = request.user
      user.first_name = form.cleaned_data['first_name']
      user.last_name = form.cleaned_data['last_name']
      image = form.cleaned_data['image']
      if image:
        f_name = save_image(image)
        profile_obj = Profile.objects.filter(user=user).first()
        if not profile_obj:
          profile_obj = Profile(user=user)
        profile_obj.image = f_name
        profile_obj.save()
      user.save()
      return redirect('/')
  else:
    form = ProfileForm(initial= {"first_name": request.user.first_name,  "last_name": request.user.last_name})
  return render(request, 'user/profile.html', {'form': form})


