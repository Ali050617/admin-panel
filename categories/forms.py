from django import forms
from .models import Category


class CategoryForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-3 py-2 text-gray-700 border rounded-lg focus:outline-none',
            'placeholder': 'Category Name'
        })
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'w-full px-3 py-2 text-gray-700 border rounded-lg focus:outline-none',
            'placeholder': 'Category Description',
            'rows': 4
        }),
        required=False
    )
    icon = forms.ImageField(
        widget=forms.FileInput(attrs={
            'class': 'w-full px-3 py-2 text-gray-700 border rounded-lg focus:outline-none'
        })
    )

    def clean_name(self):
        name = self.cleaned_data['name']
        if Category.objects.filter(name=name).exists():
            raise forms.ValidationError("A category with this name already exists.")
        return name




# class CategoryForm(forms.ModelForm):
#     class Meta:
#         model = Category
#         fields = ['name', 'description', 'icon']
#         widgets = {
#             'name': forms.TextInput(
#                 attrs={'class': 'w-full px-3 py-2 text-gray-700 border rounded-lg focus:outline-none',
#                        'placeholder': 'Product Name'}),
#             'description': forms.Textarea(
#                 attrs={'class': 'w-full px-3 py-2 text-gray-700 border rounded-lg focus:outline-none',
#                        'placeholder': 'Product Description', 'rows': 4}),
#             'price': forms.NumberInput(
#                 attrs={'class': 'w-full px-3 py-2 text-gray-700 border rounded-lg focus:outline-none',
#                        'placeholder': 'Price'}),
#             'category': forms.Select(
#                 attrs={'class': 'w-full px-3 py-2 text-gray-700 border rounded-lg focus:outline-none'}),
#             'image': forms.FileInput(
#                 attrs={'class': 'w-full px-3 py-2 text-gray-700 border rounded-lg focus:outline-none'}),
#         }
#
#     def clean_name(self):
#         name = self.cleaned_data['name']
#         if Category.objects.filter(name__iexact=name).exclude(pk=self.instance.pk).exists():
#             raise forms.ValidationError("A category with this name already exists.")
#         return name
