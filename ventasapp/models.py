from __future__ import division
from datetime import datetime
from decimal import Decimal
from django.db import models

class Sale(models.Model):
	id = models.AutoField(primary_key=True)
	date_created = models.DateTimeField('date created')
	subtotal = models.DecimalField(max_digits=10,decimal_places=2)
	tax = models.IntegerField()
	payment = models.DecimalField(max_digits=10,decimal_places=2)

	def total(self):
		sub = self.subtotal
		tx = Decimal.from_float(1+(self.tax / 100.00))
		total = (sub*tx).quantize(Decimal("0.00"))
		return total

	def change(self):
		change = (self.payment - self.total()).quantize(Decimal("0.00"))
		return change
	
	def save( self, *args, **kw ):
		if self.payment < self.total:
			self.date_created = datetime.now()
			super(Sale, self).save(*args, **kw)

	def __str__(self):
		return self.id

class Product(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=200)
	unit_cost = models.DecimalField(max_digits=10,decimal_places=2)
	unit_type = models.CharField(max_length=10, default='unit')
	def __str__(self):
		return self.name


class SalesProducts(models.Model):
	sale_id = models.ForeignKey('Sale')
	product_id = models.ForeignKey('Product')
	quanitity = models.DecimalField(max_digits=10,decimal_places=3)
