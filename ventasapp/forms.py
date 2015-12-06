from django import forms
from ventasapp.models import Sale
from ventasapp.models import Product

#from crispy_forms.helper import FormHelper
#from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
#from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['id','subtotal','tax','payment']
        error_messages = {
            'subtotal' : {
                'required' : 'Subtotal is required',
                'invalid' : 'Invalid quantity',
                'max_value' : 'Number must be higher',
                'min_value' : 'Number must be lower',
            },
            'tax' : {
            	'required' : 'Tax is required',
            	'invalid' : 'Invalid quantity',
                'max_value' : 'Number must be higher',
                'min_value' : 'Number must be lower',
            },
            'payment' : {
                'required' : 'Payment is required',
            	'invalid' : 'Invalid quantity',
                'max_value' : 'Number must be higher',
                'min_value' : 'Number must be lower',
            }
        }

class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = ['id','name','unit_cost','unit_type']