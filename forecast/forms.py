from django import forms
from .models import RequestHelp


class RequestForm(forms.ModelForm):
    """
    Request about help form
    """
    class Meta:
        model = RequestHelp
        fields = ['name', 'email', 'phone', 'subject', 'message']
