import datetime

from django.db import models
from django.utils import timezone
from picklefield.fields import PickledObjectField

class Room(models.Model):

	name =  models.CharField(max_length=200)
	description = models.CharField(max_length=2000)
		
	# one option here would be to create a separate table and have a many-to-many relationship
	dictionary = PickledObjectField()
	slug = models.SlugField()


	def __str__(self):
		return self.name
