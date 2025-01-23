from django.contrib.auth.models import User
from django.db import models
from django.db.models import (
  CharField,
  TextField,
  DateTimeField,
  ForeignKey,
  CASCADE)


class Blog(models.Model):
  title = CharField(max_length=255)
  detail = TextField()
  created_at = DateTimeField(auto_now_add=True)
  updated_at = DateTimeField(auto_now=True)
  author = ForeignKey(User, on_delete=CASCADE)

  def __str__(self):
    return self.title
