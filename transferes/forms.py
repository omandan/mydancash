from django import forms
from .models import Transfere


class CreateTransfereForm(forms.ModelForm):
    class Meta:
        model = Transfere
        fields = ['ammount','receiver']