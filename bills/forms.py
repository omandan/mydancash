from django import forms
from transferes.models import Transfere

class BillPayForm(forms.ModelForm):
    class Meta:
        model = Transfere
        fields = ['ammount']