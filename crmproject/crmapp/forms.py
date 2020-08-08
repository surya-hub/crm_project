from django import forms
from .models import Product,Order,Customer
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields =['first_name','last_name','username','password1','password2','email']

