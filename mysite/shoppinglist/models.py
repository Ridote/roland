from django.db import models

# Create your models here.
class User(models.Model):
	user_id = models.AutoField(primary_key=True)
	username = models.CharField(max_length=60)
	password = models.CharField(max_length=60)
	def __str__(self):
		return str(self.user_id) + ": " + self.username
class Product(models.Model):
	quantity = models.IntegerField(default=0)
	name = models.CharField(max_length=200)
	requester = models.ForeignKey(User, on_delete=models.CASCADE)
	def create(cls, quantity, name, requester):
		product = cls(quantity=quantity,name=name,requester=requester)
		return product
	def __str__(self):
		return self.name + ':' + str(self.quantity) + "uds"