from django.db import models
from .constants import *
class Unit(models.Model):
	name = models.CharField(max_length=MODEL_UNIT_NAME_LENGTH, unique=True)
	def __str__(self):
		return self.name
class Category(models.Model):
	name = models.CharField(max_length=MODEL_CATEGORY_NAME_LENGTH, unique=True)
	def __str__(self):
		return self.name
class PredefinedProduct(models.Model):
	name = models.CharField(max_length=MODEL_PREDEFINED_PRODUCT_NAME_LENGTH, unique=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, default=0)
	def __str__(self):
		return self.name
class Product(models.Model):
	predefinedProduct = models.ForeignKey(PredefinedProduct, on_delete=models.CASCADE, default=0)
	quantity = models.IntegerField(default=0)
	requester = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	unit = models.ForeignKey(Unit, on_delete=models.CASCADE, default=0)
	def create(cls, predefinedProduct, quantity, requester, unit):
		product = cls(predefinedProduct=predefinedProduct, quantity=quantity, requester=requester, unit= unit)
		return product
	def __str__(self):
		return self.predefinedProduct.name + ':\t' + str(self.quantity) + " " + str(self.unit.name)
