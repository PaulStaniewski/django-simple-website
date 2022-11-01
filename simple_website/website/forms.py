from django.forms import ModelForm
from .models import Gallery
from django import forms


class GalleryForm(ModelForm):  # gallery form
    class Meta:  # meta

        model = Gallery  # model
        fields = [  # fields
            "title",  # title
            "describe",  # describe
            "image"  # image
             ]


class ContactForm(forms.Form):  # contact form
    first_name = forms.CharField(max_length=50)  # first name
    last_name = forms.CharField(max_length=50)  # last name
    email_address = forms.EmailField(max_length=150)  # email address
    message = forms.CharField(widget=forms.Textarea, max_length=2000)  # message

