from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Review


class ProductForm(forms.ModelForm):

    name = forms.CharField(max_length=254)
    url = forms.SlugField(max_length=300)
    url.widget = forms.TextInput(
        attrs={'pattern': "^[a-z0-9_]+(?:-[a-z0-9_]+)*$",
               'title': "Please Enter Valid URL (No space)"})
    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    class Meta:
        model = Product
        fields = '__all__'


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('comment', 'rating')