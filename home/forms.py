from django import forms
from .models import *
from captcha.fields import ReCaptchaField


class ContactUsForm(forms.ModelForm):
    captcha = ReCaptchaField(attrs={
        'theme': 'clean',
    })

    class Meta:
        model = ContactUs
        fields = [
            "text",
            "phone_number",
            "email",
            "captcha"
        ]
