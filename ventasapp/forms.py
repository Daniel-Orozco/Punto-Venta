from django import forms
from ventasapp.models import Sale

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['id','subtotal','tax','payment']