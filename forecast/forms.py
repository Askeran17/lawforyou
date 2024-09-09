from django import forms
from .models import RequestHelp


class RequestForm(forms.ModelForm):
    """
    Request about help form
    """
    name = forms.CharField(max_length=100)
    name.widget = forms.TextInput(
        attrs={'pattern': "[A-zÀ-ú]+",
               'title': "Please Enter Valid Name (Only letters, no space)"})
    phone = forms.CharField(max_length=20)
    phone.widget = forms.TextInput(
        attrs={'pattern': "[0-9\-\+]+",
               'title': "Please Enter Valid Phone Number (Only numbers and +/-, no space)"})
    subject = forms.CharField(max_length=150)
    subject.widget = forms.TextInput(
        attrs={'pattern': "[A-zÀ-ú]+",
               'title': "Please Enter Valid Subject (Only letters, no space)"})

    class Meta:
        model = RequestHelp
        fields = ['name', 'email', 'phone', 'subject', 'message']
