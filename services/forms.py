from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Review

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'
      
    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)


class ReviewForm(forms.ModelForm):
    
    class Meta:
        model = Review
        fields = ('comment','rating')