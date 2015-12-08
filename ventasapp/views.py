from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from ventasapp.models import Sale
from ventasapp.forms import SaleForm
from ventasapp.models import Product
from ventasapp.models import Item
from ventasapp.forms import ItemForm
from datetime import datetime
from django.utils import formats

# SALES
def search(request):
    query = request.GET.get('q')
    if query:
        # There was a query entered.
        results = Product.objects.filter(name=query)
    else:
        # If no query was entered, simply return all objects
        results = Product.objects.all()
    return render(request, 'search.html', {'results': results})

def index(request):
	products = Product.objects.all()
	return render_to_response("index.html",{"ProductsParameter": products},context_instance = RequestContext(request))

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
		sal.tax = int(request.POST['tax'])
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
	query = request.GET.get('q')
	if query:
        # There was a query entered.
		results = Product.objects.filter(name=query)
	else:
   		# If no query was entered, simply return all objects
		results = None #Product.objects.all()
	items = Item.objects.all()
	date = datetime.now()
	salesID = Sale.objects.count() + 1
	return render_to_response("simulation.html",{"date": date, "sales": salesID, "ItemsParameter": items, "results": results} , context_instance = RequestContext(request))

# ITEMS
def create_item(request):
	if request.method == 'POST':
		form = ItemForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("simulation")
		else:
			pass
	else:
		form = ItemForm()
		return render_to_response("item.html", {"form":form}, context_instance = RequestContext(request))

def edit_item(request, item):
	itm = Item.objects.get(id = item)
	if request.method == 'POST':
		itm.quantity = request.POST['quantity']
		itm.save()
		return redirect("simulation")
	else:
		form = ItemForm(instance = itm)
		return render_to_response("edit_item.html", {"form":form, "item":item}, context_instance = RequestContext(request)) 

def delete_item(request, item):
    itm = Item.objects.get(id = item)
    if request.method == "POST":
        itm.delete()
        return redirect("simulation")
    else:
        return render_to_response("delete_item.html", {"item": item}, context_instance = RequestContext(request))

# PRODUCTS
def create_product(request):
	if request.method == 'POST':
		form = ProductForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("index")
	else:
		form = ProductForm()
		return render_to_response("create_product.html", {"form":form}, context_instance = RequestContext(request))

def edit_product(request, product):
	pro = Product.objects.get(id = product)
	if request.method == 'POST':
		pro.name = request.POST['name']
		pro.unit_cost = request.POST['unit_cost']
		pro.unit_type = request.POST['unit_type']
		pro.save()
		return redirect("index")
	else:
		form = ProductForm(instance = pro)
		return render_to_response("edit_product.html", {"form":form, "product":product}, context_instance = RequestContext(request)) 

def delete_product(request, product):
    pro = Product.objects.get(id = product)
    if request.method == "POST":
        pro.delete()
        return redirect("index")
    else:
        return render_to_response("delete_product.html", {"product": product}, context_instance = RequestContext(request))
