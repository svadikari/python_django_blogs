from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import EmailField, Form, CharField, ImageField
from django.core.validators import MinLengthValidator


class UserRegistrationForm(UserCreationForm):
  email = EmailField()

  class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']

class ProfileForm(Form):
  first_name = CharField(max_length=10, validators=[MinLengthValidator(2)])
  last_name = CharField(max_length=10, validators=[MinLengthValidator(2)])
  image = ImageField(label='Profile Picture', required=False)
