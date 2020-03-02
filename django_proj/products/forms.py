from .models import CellPhones
from django import forms

class CellPoneForm(forms.ModelForm):
    class Meta:
        model = CellPhones
        fields = '__all__'