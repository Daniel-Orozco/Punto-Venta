from django import forms
from ventasapp.models import Sale

#from crispy_forms.helper import FormHelper
#from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
#from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['id','subtotal','tax','payment']