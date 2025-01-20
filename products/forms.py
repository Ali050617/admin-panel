from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category', 'image']
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'w-full px-3 py-2 text-gray-700 border rounded-lg focus:outline-none',
                       'placeholder': 'Product Name'}),
            'description': forms.Textarea(
                attrs={'class': 'w-full px-3 py-2 text-gray-700 border rounded-lg focus:outline-none',
                       'placeholder': 'Product Description', 'rows': 4}),
            'price': forms.NumberInput(
                attrs={'class': 'w-full px-3 py-2 text-gray-700 border rounded-lg focus:outline-none',
                       'placeholder': 'Price'}),
            'category': forms.Select(
                attrs={'class': 'w-full px-3 py-2 text-gray-700 border rounded-lg focus:outline-none'}),
            'image': forms.FileInput(
                attrs={'class': 'w-full px-3 py-2 text-gray-700 border rounded-lg focus:outline-none'}),
        }

    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0:
            raise forms.ValidationError("Price must be greater than zero.")
        return price
