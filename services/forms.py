from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Review


class ProductForm(forms.ModelForm):

    name = forms.CharField(max_length=254)
    name.widget = forms.TextInput(
        attrs={'pattern': "[A-zÀ-ú]+",
               'title': "Please Enter Valid Name (Only letters, no space)"})

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('comment', 'rating')