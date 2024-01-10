from django import forms  
from django.contrib.auth.models import User  
from django.core.validators import EmailValidator
from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.forms import ModelForm
from django.forms.widgets import FileInput
from .models import *
import re

class AuthenticationForm(forms.Form):
    username = forms.CharField(max_length = 30)
    password = forms.CharField(max_length = 30, widget = forms.PasswordInput)
    class Meta:
        fields = ['username', 'password']
# class ItemFilterForm(forms.Form):
#     class Meta:
#         model = cars
#         fields = ['name', 'price']

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True, validators=[EmailValidator()])
    password1 = forms.CharField(max_length=30, required=True, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=30, required=True, widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('This username is already taken.')
        return username

    def clean_password2(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('The passwords do not match.') 
        return 

    def clean_password1(self):
        cleaned_data = super().clean()
        password1 = self.cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if len(password1) < 8:
            raise forms.ValidationError("Password must contain at least 8 characters")
        if not re.search('[A-Z]', password1):
            raise forms.ValidationError("Password must contain at least one uppercase letter")
        if not re.search('[a-z]', password1):
            raise forms.ValidationError("Password must contain at least one lowercase letter")
        if not re.search('[0-9]', password1):
            raise forms.ValidationError("Password must contain at least one number")
        return password1 
  
    def clean_email(self):  
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email Already Exist.")
        return email  

# class ProfileForm(UserChangeForm, forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ('bio', 'location', 'birth_date')

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['bio'].widget.attrs.update({'class': 'form-control'})
#         self.fields['location'].widget.attrs.update({'class': 'form-control'})
#         self.fields['birth_date'].widget.attrs.update({'class': 'form-control', 'placeholder': 'YYYY-MM-DD'})


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']
        widgets = {
            'profile_img': FileInput(),
        }

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_pic'] 

class PriceFilterForm(forms.Form):
    min_price = forms.DecimalField(max_digits=6, decimal_places=2, required=False)
    max_price = forms.DecimalField(max_digits=6, decimal_places=2, required=False)