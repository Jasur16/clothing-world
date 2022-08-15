from django import forms
# from .models import ContactModel
# from django.core.validators import MaxLengthValidator
from django.utils.translation import gettext_lazy as _
from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    phone = forms.CharField(max_length=13)
    message = forms.CharField(widget=forms.Textarea, help_text="Message...")


# class ContactForm(forms.ModelForm):
#     class Meta:
#         model = ContactModel
#         exclude = ['created_at']


class ContactForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    phone = forms.CharField(max_length=13)
    message = forms.CharField(widget=forms.Textarea, help_text="Message...")
