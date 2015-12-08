from __future__ import division
from datetime import datetime
from decimal import Decimal
from django.db import models

class Sale(models.Model):

	id = models.AutoField(primary_key=True)
	date_created = models.DateTimeField('date created')
	subtotal = models.DecimalField(max_digits=10,decimal_places=2)
	tax = models.IntegerField(default=10)
	payment = models.DecimalField(max_digits=10,decimal_places=2)
	total = models.DecimalField(max_digits=10,decimal_places=2,default=0.00)

	def change(self):
		change = (self.payment - self.total).quantize(Decimal("0.00"))
		return change
	
	def save( self, *args, **kw ):
		self.total = self.subtotal
		if self.payment >= self.total:
			Cashier.objects.get(id=1).add_cash(self.total)
			self.date_created = datetime.now()
			super(Sale, self).save(*args, **kw)

	def __str__(self):
		return self.id

	def __unicode__(self):
		return unicode(self.tax)

class Product(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=200)
	unit_cost = models.DecimalField(max_digits=10,decimal_places=2)
	unit_type = models.CharField(max_length=10, default='unit')
	
	def __str__(self):
		return self.name

class Item(models.Model):
	sale_id = models.ForeignKey('Sale')
	product_id = models.ForeignKey('Product')
	quantity = models.DecimalField(max_digits=10,decimal_places=3)
	total = models.DecimalField(max_digits=10,decimal_places=2,default=0.00)

	def save( self, *args, **kw ):
		if self.quantity > 0:
			last_sale = Sale.objects.latest('id')
			exists = Item.objects.filter(product_id = self.product_id, sale_id=last_sale.id).first()
			if exists is None:
				self.sale_id = last_sale
			else:
				self.quantity+=exists.quantity
				self.sale_id = exists.sale_id
				exists.delete()
			self.total = Decimal(self.product_id.unit_cost) * Decimal(self.quantity)
			super(Item, self).save(*args, **kw)

	def __str__(self):
		return self.id

	def __unicode__(self):
		return unicode(self.product_id)

class Cashier(models.Model):
	id = models.AutoField(primary_key=True)
	cash = models.DecimalField(max_digits=10,decimal_places=2,default='min_cash')
	min_cash = models.DecimalField(max_digits=10,decimal_places=2,default=200)
	max_cash = models.DecimalField(max_digits=10,decimal_places=2,default=1000)
	withdrawal = models.IntegerField(default=0)
	tax = models.IntegerField(default=10)
	
	def add_cash(self,amount):
		self.cash += Decimal(amount)
		if(self.cash > Decimal(self.max_cash)):
			self.withdrawal+= (Decimal(self.cash) - Decimal(self.min_cash))
			self.cash = self.min_cash
		self.save()
		
	def return_cash(self,amount):
		if(self.cash-self.min_cash < amount):
			amount -= self.cash + self.min_cash
			self.cash = self.min_cash
			self.withdrawal -= amount
	
	def save( self, *args, **kw):
		if (float(self.min_cash) < float(self.max_cash) and float(self.min_cash) > 0.00 and float(self.max_cash) > 0.00):
			super(Cashier,self).save(*args,**kw)
			
	def __str__(self):
		return int(self.id)
