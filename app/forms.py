from django import forms
from django.contrib.auth.models import User
from app.models import Transaction


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ["date", "amount", "description", "transaction_type"]

    def __init__(self, *args, **kwargs):
        super(TransactionForm, self).__init__(*args, **kwargs)
        self.fields["date"].label = "Fecha"
        self.fields["amount"].label = "Monto"
        self.fields["description"].label = "Descripción"
        self.fields["transaction_type"].label = "Tipo de transacción"


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = (
            "username",
            "password",
        )
