from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE


class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=CASCADE)
  image = models.TextField(default='default.png')

  def __str__(self):
    return f'{self.user.username} profile'
