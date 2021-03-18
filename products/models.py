from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)


class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey('products.Category', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=100000, decimal_places=2)
