from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)


class RegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(max_length=16, required=True, widget=forms.PasswordInput)

    # username = forms.CharField(
    #     max_length=50,
    #     min_length=4,
    #     widget=forms.TextInput
    # )
    # first_name = forms.CharField(
    #     max_length=50,
    #     min_length=4,
    #     widget=forms.TextInput
    # )
    # last_name = forms.CharField(
    #     max_length=50,
    #     min_length=4,
    #     widget=forms.TextInput
    # )
    # password = forms.CharField(
    #     max_length=16,
    #     min_length=8,
    #     widget=forms.PasswordInput
    # )
    # confirm_password = forms.CharField(
    #     max_length=16,
    #     min_length=8,
    #     widget=forms.PasswordInput
    # )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password', 'confirm_password')

    def clean_confirm_password(self):
        data = super(RegistrationForm, self).clean()
        if data.get('password') != data.get('confirm_password'):
            raise ValidationError('Пароли не совпадают!')
        return data
