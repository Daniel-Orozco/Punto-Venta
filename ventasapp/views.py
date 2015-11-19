from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from crudapp.models import Sale
from crudapp.forms import SaleForm

# Create your views here.
def index(request):
	sales = Sale.objects.all()
	return render_to_response("index.html",{"SalesParameter": sales},context_instance = RequestContext(request))

def show_sale(request, sale):
	sal = Sale.objects.get(id = sale)
	return render_to_response("show_sale.html",{"sale":sal},context_instance = RequestContext(request))

