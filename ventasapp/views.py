from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from ventasapp.models import Sale
from ventasapp.forms import SaleForm
from datetime import datetime
from django.utils import formats

# SALES

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
		form = SaleForm()
		return render_to_response("sales.html", {"form":form}, context_instance = RequestContext(request))

def edit_sale(request, sale):
	sal = Sale.objects.get(id = sale)
	if request.method == 'POST':
		sal.subtotal = request.POST['subtotal']
		sal.payment = request.POST['payment']
		sal.tax = request.POST['tax']
		sal.save()
		return redirect("list_sales")
	else:
		form = SaleForm(instance = sal)
		return render_to_response("edit_sale.html", {"form":form, "sale":sale}, context_instance = RequestContext(request)) 

def delete_sale(request, sale):
    sal = Sale.objects.get(id = sale)
    if request.method == "POST":
        sal.delete()
        return redirect("list_sales")
    else:
        return render_to_response("delete_sale.html", {"sale": sale}, context_instance = RequestContext(request))

def list_sales(request):
	sales = Sale.objects.all()
	return render_to_response("list_sales.html",{"SalesParameter": sales},context_instance = RequestContext(request))

def simulation(request):
	date = datetime.now()
	salesID=Sale.objects.count() + 1
	return render_to_response("simulation.html",{"date": date, "sales": salesID} , context_instance = RequestContext(request))