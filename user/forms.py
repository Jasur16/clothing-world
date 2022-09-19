from django import forms
from .models import UserModel, ProfileModel
from django.utils.translation import gettext_lazy as _
from django.core.validators import ValidationError


class ProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        exclude = ['user', 'created_at']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'First Name',
                'class': 'stext-111 cl8 plh3 size-111 p-lr-15',
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Last Name',
                'class': 'stext-111 cl8 plh3 size-111 p-lr-15',
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': 'Phone Number',
                'class': 'stext-111 cl8 plh3 size-111 p-lr-15',
            }),
            'city': forms.TextInput(attrs={
                'placeholder': 'City',
                'class': 'stext-111 cl8 plh3 size-111 p-lr-15',
            }),
            'address': forms.Textarea(attrs={
                'placeholder': 'Address',
                'class': 'stext-111 cl8 plh3 size-111 p-lr-15 pt-2',
            }),
            'email': forms.TextInput(attrs={
                'placeholder': 'Email',
                'class': 'stext-111 cl8 plh3 size-111 p-lr-15',
            })
        }


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
