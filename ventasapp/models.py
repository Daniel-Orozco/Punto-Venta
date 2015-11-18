from django.db import models

class Sale(models.Model):
    date_created = models.DateTimeField('date created')
    subtotal = models.DecimalField(decimal_places=2)
    tax = models.IntegerField()
    payment = models.DecimalField(decimal_places=2)


class Product(models.Model):
    name = models.CharField(max_length=200)
    unit_cost = models.DecimalField(decimal_places=2)


class Sales-Products(models.Model):
    sale_id = models.ForeignKey('Sale')
    product_id = models.ForeignKey('Product')
    quanitity = models.DecimalField(decimal_places=3)
