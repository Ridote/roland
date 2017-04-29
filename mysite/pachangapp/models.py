from django.db import models
from .constants import *
from datetime import date, datetime

class Match(models.Model):
	date = models.DateTimeField('date')
	duration = models.TimeField('duration')
	team_home = models.ManyToManyField('auth.User', related_name='home_team')
	team_visitant = models.ManyToManyField('auth.User', related_name='visitors')
	def played(self):
		return date >= datetime.now()
	def __str__(self):
		return 'Date:' + str(self.date) + '. Duration: ' + str(self.duration) + ". "