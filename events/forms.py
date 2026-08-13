from django import forms
from .models import SupportRequest

class SupportRequestForm(forms.ModelForm):

    class Meta:
        model = SupportRequest
        fields = [
            "name",
            "phone",
            "email",
            "subject",
            "message",
        ]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "placeholder": "Your Name",
                    "class": "form-control",
                }
            ),
            "phone": forms.TextInput(
                attrs={
                    "placeholder": "Phone Number",
                    "class": "form-control",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "placeholder": "Email Address",
                    "class": "form-control",
                }
            ),

            "subject": forms.TextInput(
                attrs={
                    "placeholder": "Subject",
                    "class": "form-control",
                }
            ),

            "message": forms.Textarea(
                attrs={
                    "placeholder": "How can we help you?",
                    "class": "form-control",
                    "rows": 5,
                }
            ),
        }