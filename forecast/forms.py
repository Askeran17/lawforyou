from django import forms
from .models import RequestHelp


class RequestForm(forms.ModelForm):
    """
    Request about help form
    """
    name = forms.CharField(max_length=100, required=True)
    name.widget = forms.TextInput(
        attrs={'pattern': "[A-zÀ-ú]+",
               'title': "Please Enter Valid Name (Only letters, no space)"})
    subject = forms.CharField(max_length=150)
    subject.widget = forms.TextInput(
        attrs={'pattern': "[A-zÀ-ú]+",
               'title': "Please Enter Valid Subject (Only letters, no space)"})

    class Meta:
        model = RequestHelp
        fields = ['name', 'email', 'phone', 'subject', 'message']

    def __init__(self, *args, **kwargs):
        """
        Initialize class to fields
        """
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = (
                'border-dark')