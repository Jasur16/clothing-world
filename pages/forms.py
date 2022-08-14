from django import forms
from .models import ContactModel
from django.core.validators import MaxLengthValidator


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        exclude = ['created_at']

