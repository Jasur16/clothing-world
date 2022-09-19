from django import forms
from .models import ColorModel
#
#
# class CheckoutForm(forms.ModelForm):
#     full_name = forms.CharField(widget=forms.TextInput(attrs={
#         'placeholder': 'Full name',
#         'class': 'stext-111 cl8 plh3 size-111 p-lr-15'
#     }))
#     phone = forms.CharField(widget=forms.TextInput(attrs={
#         'placeholder': 'Phone Number',
#         'class': 'stext-111 cl8 plh3 size-111 p-lr-15'
#     }))
#     address = forms.CharField(widget=forms.Textarea(attrs={
#         'placeholder': 'Address',
#         'class': 'stext-111 cl8 plh3 size-111 p-lr-15'
#     }))
#     comment = forms.CharField(widget=forms.Textarea(attrs={
#         'placeholder': 'Comment',
#         'class': 'stext-111 cl8 plh3 size-111 p-lr-15',
#     }))
#
#     class Meta:
#         model = ShopHistoryModel
#         exclude = ['user', 'products', 'created_at']


class ColorModelAdminForms(forms.ModelForm):
    code = forms.CharField(widget=forms.TextInput(attrs={'type': 'color'}))

    class Meta:
        model = ColorModel
        fields = '__all__'
