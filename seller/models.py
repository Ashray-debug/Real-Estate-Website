from django.db import models

class Realtor(models.Model):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	username = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	password = models.CharField(max_length=200)
	password2 = models.CharField(max_length=200)
	def __str__(self):
		return self.username