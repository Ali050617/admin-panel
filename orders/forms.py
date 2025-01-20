from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['status', 'total_amount']
        widgets = {
            'status': forms.Select(attrs={'class': 'w-full px-3 py-2 text-gray-700 border rounded-lg focus:outline-none'}),
        }

    def clean_total_amount(self):
        total_amount = self.cleaned_data['total_amount']
        if total_amount <= 0:
            raise forms.ValidationError("Total amount must be greater than zero.")
        return total_amount