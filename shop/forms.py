from django import forms
from .models import ColorModel, ShopHistoryModel


class CheckoutForm(forms.ModelForm):

    class Meta:
        model = ShopHistoryModel
        exclude = ['user', 'products', 'created_at']


class ColorModelAdminForms(forms.ModelForm):
    code = forms.CharField(widget=forms.TextInput(attrs={'type': 'color'}))

    class Meta:
        model = ColorModel
        fields = '__all__'
