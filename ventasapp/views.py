from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from ventasapp.models import Sale
from ventasapp.forms import SaleForm
from ventasapp.models import Product
from ventasapp.models import Item
from ventasapp.models import Cashier
from ventasapp.forms import CashForm
from ventasapp.forms import ItemForm
from django.db.models import Sum
from django.utils import timezone
from django.utils import formats
from decimal import Decimal

# SALES
'''
def search(request):
    query = request.GET.get('q')
    if query:
        # There was a query entered.
        results = Product.objects.filter(name=query)
    else:
        # If no query was entered, simply return all objects
        results = Product.objects.all()
    return render(request, 'search.html', {'results': results})
'''

def index(request):
	products = Product.objects.all()
	cc = Cashier.objects.filter(id=1).first()
	if cc is None:
		cc = Cashier()
		cc.id = 1
		cc.cash = 200
		cc.save()
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
		
def edit_settings(request, cashier):
	register = Cashier.objects.get(id=1)
	cashier = 1
	if(request.method == 'POST'):
		register.min_cash = request.POST['min_cash']
		register.max_cash = request.POST['max_cash']
		register.cash = register.min_cash
		register.tax = request.POST['tax']
		register.save()
		return redirect("index")
	else:
		form = CashForm(instance = register)
		return render_to_response("edit_settings.html",{"form":form, "cashier": cashier}, context_instance = RequestContext(request))

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

# SIMULATION
def simulation(request):
	query = request.GET.get('q')
	if query:
        # There was a query entered.
		results = Product.objects.filter(name=query)
	else:
   		# If no query was entered, simply return all objects
		results = None #Product.objects.all()
	items = Item.objects.all()
	date = timezone.now()
	SID = Sale.objects.latest('id')
	if SID is not None:
		salesID = SID.id+1
	else:
		salesID = 1
	subtotal = items.aggregate(Sum('total')).values()[0]
	cash = Cashier.objects.get(id=1)
	tax = Decimal.from_float((float(cash.tax)/100)).quantize(Decimal("0.00"))
	if subtotal is not None:
		total = (subtotal*(1+tax)).quantize(Decimal("0.00"))
	else:
		total = 0.00
	tax *= 100
	session = Sale(date_created = timezone.now(), subtotal = subtotal, tax = tax, payment = total, total = total)
	form = SaleForm(request.POST, instance=session)
	return render_to_response("simulation.html",{"form":form,"date": date, "sales": salesID, "ItemsParameter": items, "subtotal": subtotal, "tax":tax, "total":total} , context_instance = RequestContext(request))

def finish_simulation(request):
	if request.method == 'POST':
		subtotal = request.POST.get('subtotal')
		payment = request.POST['payment']
		tax = request.POST.get('tax')
		total = request.POST.get('total')
		dlt = Sale.objects.latest('id')
		i = dlt.id
		dlt.delete()
		sim = Sale(id = i, date_created = timezone.now(), subtotal = subtotal, tax = tax, payment = total, total = total)
		if sim is not None:
			sim.save()
			return redirect("index")
		else:
			return redirect("simulation")
# ITEMS
def create_item(request):
	if request.method == 'POST':
		form = ItemForm(request.POST)
		if form.is_valid():
			form.save()
			print form
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
