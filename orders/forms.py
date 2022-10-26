from django import forms
from .models import OrderHistoryModel


class CheckoutForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'First name',
        'class': 'stext-111 cl8 plh3 size-111 p-lr-15'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Last name',
        'class': 'stext-111 cl8 plh3 size-111 p-lr-15'
    }))
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Phone Number',
        'class': 'stext-111 cl8 plh3 size-111 p-lr-15'
    }))
    city = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'City',
        'class': 'stext-111 cl8 plh3 size-111 p-lr-15'
    }))
    address = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Address',
        'class': 'stext-111 cl8 plh3 size-111 p-lr-15'
    }))
    gmail = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your email',
        'class': 'stext-111 cl8 plh3 size-111 p-lr-15'
    }))
    comment = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Comment',
        'class': 'stext-111 cl8 plh3 size-111 p-lr-15',
    }))

    class Meta:
        model = OrderHistoryModel
        exclude = ['user', 'products', 'created_at']
