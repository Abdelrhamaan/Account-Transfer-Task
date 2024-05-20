# forms.py
from django import forms
from .models import Accounts


class TransferForm(forms.Form):
    from_user = forms.ModelChoiceField(
        queryset=Accounts.objects.all(),
        label="From User",
        widget=forms.Select(attrs={'class': 'form-select cust-font'}),
        label_suffix=""
    )
    to_user = forms.ModelChoiceField(
        queryset=Accounts.objects.all(),
        label="To User",
        widget=forms.Select(attrs={'class': 'form-select cust-font'}),
        label_suffix=""
    )
    amount = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        label="Amount",
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        label_suffix=""
    )

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if not amount:
            raise forms.ValidationError(
                "You should add the transfered amount.")
        if amount <= 0:
            raise forms.ValidationError(
                "The amount must be greater than zero.")
        return amount

    def clean_to_user(self):
        from_user = self.cleaned_data.get('from_user')
        to_user = self.cleaned_data.get('to_user')
        if from_user == to_user:
            raise forms.ValidationError(
                "You cannot transfer amount to the same user"
            )
        return to_user
