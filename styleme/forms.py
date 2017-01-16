from django import forms
# from .models import Styleme, Clothing_Item
from django.db import models
from django.contrib.auth.models import User
from views import ClothingItem



class UserPostForm(forms.ModelForm):
    class Meta:
        model = ClothingItem
        fields = ('image', 'name')
