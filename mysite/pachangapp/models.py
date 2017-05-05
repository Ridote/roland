from django.db import models
from .constants import *
from datetime import date, datetime
class Group(models.Model):
	name = models.CharField(max_length=MODEL_GROUP_NAME)
	def __str__(self):
		return self.name
class City(models.Model):
	name = models.CharField(max_length=MODEL_CITY_NAME, default="")
	def __str__(self):
		return self.name
class Arena(models.Model):
	name = models.CharField(max_length=MODEL_ARENA_NAME, default="")
	city = models.ForeignKey(City, on_delete=models.CASCADE)
	def __str__(self):
		return self.name
class Stats(models.Model):
	atack = models.PositiveSmallIntegerField()
	defense = models.PositiveSmallIntegerField()
	sustain = models.PositiveSmallIntegerField()
	teamplay = models.PositiveSmallIntegerField()
	speed = models.PositiveSmallIntegerField()
	def __str__(self):
		return '(ATK:' + str(self.atack) + ', DEF:' + str(self.defense) + ', SUS:' + str(self.sustain) + ', TPL:' + str(self.teamplay) + ', SPD:' +  str(self.speed) + ')'

class User(models.Model):
	user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
	stats = models.OneToOneField(Stats, on_delete=models.CASCADE)
	known_as = models.CharField(max_length=MODEL_USER_KNOWN_AS, default="")
	groups = models.ManyToManyField(Group)
	country = models.CharField(
		max_length = 2,
        choices = MODEL_USER_COUNTRIES,
        default = 'ND'
    )
	avatar = models.ImageField(blank=True, null=True)
	def __str__(self):
		return self.user.username.title() + " " + self.known_as
class Match(models.Model):
	date = models.DateTimeField('date')
	duration = models.TimeField('duration')
	arena = models.ForeignKey(Arena, on_delete=models.CASCADE)
	team_home = models.ManyToManyField(User, related_name='home_team')
	team_visitor = models.ManyToManyField(User, related_name='visitors')
	def played(self):
		return date >= datetime.now()
	def __str__(self):
		return 'Date:' + str(self.date) + '. Duration: ' + str(self.duration) + ". "