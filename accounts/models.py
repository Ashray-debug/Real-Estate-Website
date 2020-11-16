from django.db import models
from datetime import datetime
from realtors.models import Realtor


class Realtor(models.Model):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	username = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	password = models.CharField(max_length=200)
	password2 = models.CharField(max_length=200)
	def __str__(self):
		return self.username  


class Listings(models.Model):
	address = models.CharField(max_length=200)
	city = models.CharField(max_length=200)
	state = models.CharField(max_length=200)
	zipcode = models.CharField(max_length=200)
	description = models.TextField(blank=True)
	price = models.IntegerField()
	bedrooms = models.IntegerField()
	bathrooms = models.DecimalField(max_digits=2 ,decimal_places=1)
	garage = models.IntegerField(default=0)
	sqft = models.IntegerField()
	lot_size = models.DecimalField(max_digits=5 ,decimal_places=1)
	photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
	photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
	photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
	photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
	photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
	photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
	photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
	list_date = models.DateTimeField(default=datetime.now,blank=True)
	def __str__(self):
		return self.address