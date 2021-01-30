from django import forms
from .models import product


class productForm(forms.ModelForm):
    ProductName = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", 'name': 'ProductName', 'placeholder': "Product Name"}))
    Price = forms.CharField(widget=forms.NumberInput(attrs={"class": "form-control", 'name': 'Price', 'placeholder': "Product Price"}))
    Stock = forms.CharField(widget=forms.NumberInput(attrs={"class": "form-control", 'name': 'Stock', 'placeholder': "Product Stock"}))
    class Meta:
        model = product
        fields = ['ProductName', 'ProducImage', 'Price', 'Stock']
