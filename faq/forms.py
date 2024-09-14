from django import forms
from .models import LawFaq


class FaqForm(forms.ModelForm):
    """
    Form for FAQ
    """
    class Meta:
        model = LawFaq
        fields = '__all__'
