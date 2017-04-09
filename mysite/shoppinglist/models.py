from django.db import models

class Product(models.Model):
	quantity = models.IntegerField(default=0)
	name = models.CharField(max_length=200)
	requester = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	def create(cls, quantity, name, requester):
		product = cls(quantity=quantity,name=name,requester=requester)
		return product
	def __str__(self):
		return self.name + ':' + str(self.quantity) + " uds"