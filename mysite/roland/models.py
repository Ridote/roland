from django.db import models
from .constants import *
from datetime import date, datetime

class Publication(models.Model):
	title = models.CharField(max_length=MODEL_PUBLICATION_TITLE_LENGTH)
	content = models.TextField(max_length=MODEL_PUBLICATION_CONTENT_LENGTH)
	pub_date = models.DateTimeField('date published')
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	def published(self):
		return pub_date >= datetime.now()
	def __str__(self):
		return '(' + self.author.username + ') ' + self.title + '. ' + str(self.pub_date)