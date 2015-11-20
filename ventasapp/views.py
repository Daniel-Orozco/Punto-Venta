from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from ventasapp.models import Sale
from ventasapp.forms import SaleForm

# Create your views here.
def index(request):
	sales = Sale.objects.all()
	return render_to_response("index.html",{"SalesParameter": sales},context_instance = RequestContext(request))

def show_sale(request, sale):
	sal = Sale.objects.get(id = sale)
	return render_to_response("show_sale.html",{"sale":sal},context_instance = RequestContext(request))

def create_sale(request):
	if request.method == 'POST':
		form = SaleForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("list_sales")
		else:
			return HttpResponse("Error")
	else:
		form = SaleForm()
		return render_to_response("sales.html", {"form":form}, context_instance = RequestContext(request))

def list_sales(request):
	sales = Sale.objects.all()
	return render_to_response("list_sales.html",{"SalesParameter": sales},context_instance = RequestContext(request))