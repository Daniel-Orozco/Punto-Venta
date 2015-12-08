from django import forms
from ventasapp.models import Sale
from ventasapp.models import Product
from ventasapp.models import Item
from ventasapp.models import Cashier

#from crispy_forms.helper import FormHelper
#from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
#from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

class SaleForm(forms.ModelForm):
    class Meta:
    	model = Sale
    	fields = ['id','subtotal', 'payment']

class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = ['id','name','unit_cost','unit_type']

class ItemForm(forms.ModelForm):
	class Meta:
		model = Item
		fields = ['product_id','quantity']

class CashForm(forms.ModelForm):
	class Meta:
		model = Cashier
		fields = ['id', 'min_cash', 'max_cash']
