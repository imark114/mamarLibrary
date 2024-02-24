from django import forms
from .models import Transaction
class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = [
            'amount',
        ]
    
    def clean(self):
        cleaned_data = super().clean()
        amount = cleaned_data.get('amount')
        if amount < 0:
            raise forms.ValidationError("Deposit amount must be positive.")
        return cleaned_data