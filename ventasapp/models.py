from django.db import models

class Sale(models.Model):
	id = models.AutoField(primary_key=True)
	date_created = models.DateTimeField('date created')
	subtotal = models.DecimalField(max_digits=10,decimal_places=2)
	tax = models.IntegerField()
	payment = models.DecimalField(max_digits=10,decimal_places=2)

	def __str__(self):
		return self.id

class Product(models.Model):
    name = models.CharField(max_length=200)
    unit_cost = models.DecimalField(max_digits=10,decimal_places=2)


class SalesProducts(models.Model):
    sale_id = models.ForeignKey('Sale')
    product_id = models.ForeignKey('Product')
    quanitity = models.DecimalField(max_digits=10,decimal_places=3)
