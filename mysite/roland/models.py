from django.db import models
from .constants import *
from datetime import date, datetime

# Administration and blog
class Publication(models.Model):
	title = models.CharField(max_length=MODEL_PUBLICATION_TITLE_LENGTH)
	content = models.TextField(max_length=MODEL_PUBLICATION_CONTENT_LENGTH)
	pub_date = models.DateTimeField('date published')
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	def published(self):
		return pub_date >= datetime.now()
	def __str__(self):
		return '(' + self.author.username + ') ' + self.title + '. ' + str(self.pub_date)

#Forum

# Rol definition
class Manual(models.Model):
	title = models.CharField(max_length=MODEL_MANUAL_TITLE_LENGTH)
	description = models.TextField(max_length=MODEL_MANUAL_DESCRIPTION_LENGTH)
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	def __str__(self):
		return '(' + self.author.username + ') ' + self.title
class Category(models.Model):
	name = models.CharField(max_length=MODEL_CATEGORY_NAME_LENGTH)
	content = models.TextField(max_length=MODEL_CATEGORY_CONTENT_LENGTH)
	superCategory = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
	manual  = models.ForeignKey(Manual, on_delete=models.CASCADE)
	def __str__(self):
		return self.name
