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
class Religion(models.Model):
	name = models.CharField(max_length=MODEL_RELIGION_TITLE_LENGTH)
	content = models.TextField(max_length=MODEL_RELIGION_CONTENT_LENGTH)

class Manual(models.Model):
	title = models.CharField(max_length=MODEL_MANUAL_TITLE_LENGTH)
	description = models.TextField(max_length=MODEL_MANUAL_DESCRIPTION_LENGTH)
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	religion = models.ForeignKey(Religion, on_delete=models.CASCADE)
	def __str__(self):
		return '(' + self.author.username + ') ' + self.title