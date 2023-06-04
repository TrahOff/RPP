from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import OrderInfo


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput())
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput())
    first_name = forms.CharField(label='Имя', widget=forms.TextInput())
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput())
    email = forms.CharField(label='Почта', widget=forms.EmailInput())

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'email')
        widgets = {
            'username': forms.TextInput(),
            'password1': forms.PasswordInput(),
            'password2': forms.PasswordInput(),
            'first_name': forms.TextInput(),
            'last_name': forms.TextInput(),
            'email': forms.EmailInput(),
        }


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput())
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput())


class RegisterOrderForm(forms.ModelForm):
    class Meta:
        model = OrderInfo
        fields = [
            'order',
            'recipient_first_name',
            'recipient_email',
            'recipient_phone_number',
            'recipient_address',
            'delivery_method',
            'discount'
        ]
        widgets = {
            "order": forms.TextInput(attrs={'type': 'hidden'}),
            "recipient_first_name": forms.TextInput(attrs={'type': 'text', 'placeholder': 'Имя'}),
            "recipient_email": forms.EmailInput(attrs={'type': 'text', 'placeholder': 'Email'}),
            "recipient_phone_number": forms.TextInput(attrs={'type': 'text', 'placeholder': 'Телефон'}),
            "recipient_address": forms.TextInput(attrs={'type': 'hidden'}),
            "delivery_method": forms.Select(),
            "discount": forms.CheckboxInput()
        }
