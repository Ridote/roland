from django.db import models

class Unity(models.Model):
	name = models.CharField(max_length=8, unique=True)
	def __str__(self):
		return self.name
class PredefinedProduct(models.Model):
	name = models.CharField(max_length=200, unique=True)
	def __str__(self):
		return self.name
class Product(models.Model):
	name = models.CharField(max_length=200, unique=True)
	quantity = models.IntegerField(default=0)
	requester = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	unity = models.ForeignKey(Unity, on_delete=models.CASCADE)
	def create(cls, name, quantity, unity, requester):
		product = cls(name=name, quantity=quantity, unity=unity, requester=requester)
		return product
	def __str__(self):
		return self.name + ':\t' + str(self.quantity) + str(self.unity)
