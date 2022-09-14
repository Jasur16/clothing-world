from django import forms
from .models import UserModel
from django.utils.translation import gettext_lazy as _
from django.core.validators import ValidationError


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': _('Имя пользователя'),
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': _('Пароль'),
    }))


# class RegistrationForm(forms.Form):
#     first_name = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control',
#         'placeholder': _('Имя')
#     }))
#     last_name = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control',
#         'placeholder': _('Фамилия')
#     }))
#     username = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control',
#         'placeholder': _('Имя пользователя')
#     }))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={
#         'class': 'form-control',
#         'placeholder': _('Пароль')
#     }))
#     confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
#         'class': 'form-control',
#         'placeholder': _('Подтвердить Пароль')
#     }))
#
#     def clean_confirm_password(self, *args, **kwargs):
#         if self.cleaned_data['confirm_password'] != self.cleaned_data['password']:
#             raise ValidationError(_('Пароли не совпадают!'))
#         return self.cleaned_data
#
#     class Meta:
#         model = UserModel
#         # fields = ['first_name', 'last_name', 'username', 'password', 'confirm_password']


class RegistrationForm(forms.ModelForm):
    first_name = forms.CharField(widget=(
        forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': _('Имя'),
        })
    ), required=True)
    last_name = forms.CharField(widget=(
        forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': _('Фамилия'),
        })
    ), required=True)
    username = forms.CharField(widget=(
        forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': _('Имя пользователя'),
        })
    ), required=True)
    password = forms.CharField(widget=(
        forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': _('Пароль'),
        })
    ), required=True)
    confirm_password = forms.CharField(widget=(
        forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': _('Подтвердить Пароль'),
        })
    ), required=True)

    def clean_confirm_password(self, *args, **kwargs):
        if self.cleaned_data['confirm_password'] != self.cleaned_data['password']:
            raise ValidationError('Пароли не совпадают!')
        return self.cleaned_data

    class Meta:
        model = UserModel
        fields = ['first_name', 'last_name', 'username', 'password', 'confirm_password']