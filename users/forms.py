from django import forms
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from .models import UserModel
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=50,
        widget=forms.TextInput,
        label=_('Username')
    )
    password = forms.CharField(
        max_length=32,
        widget=forms.PasswordInput,
        label=_('Password')
    )


class RegistrationForm(forms.Form):
    username = forms.CharField(
        max_length=50,
        min_length=4,
        label=_('Username'),
        widget=forms.TextInput,
    )
    first_name = forms.CharField(
        max_length=50,
        label=_('First name'),
        widget=forms.TextInput
    )
    last_name = forms.CharField(
        max_length=50,
        label=_('Last name'),
        widget=forms.TextInput
    )
    password = forms.CharField(
        max_length=32,
        min_length=8,
        label=_('Password'),
        widget=forms.PasswordInput
    )
    confirm_password = forms.CharField(
        max_length=32,
        min_length=8,
        label=_('Confirm password'),
        widget=forms.PasswordInput
    )

    def clean_username(self):
        data = super(RegistrationForm, self).clean()
        username = data.get('username')
        user = User.objects.all().filter(username=username)
        if user:
            raise ValidationError('Ushbu username band !')
        return data

    def clean_confirm_password(self):
        data = super(RegistrationForm, self).clean()
        if data.get('password') != data.get('confirm_password'):
            raise ValidationError("Parollar bir hil emas !")
        return data
