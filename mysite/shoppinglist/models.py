from django.db import models

# Create your models here.
class User(models.Model):
	username = models.CharField(max_length=60)
	password = models.CharField(max_length=60)

class Product(models.Model):
	quantity = models.IntegerField(default=0)
	name = models.CharField(max_length=200)
	requester = models.ForeignKey(User, on_delete=models.CASCADE)