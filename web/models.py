from __future__ import unicode_literals

from django.db import models
from django.core.files.storage import FileSystemStorage


fs = FileSystemStorage(location='media/')

# Create your models here.
class CarouselCaption(models.Model):
	caption = models.CharField(max_length=100)
	publish_date = models.DateField()

	def __str__(self):
		return self.caption

class About(models.Model):
	description = models.CharField(max_length=500)
	publish_date = models.DateField()

	def __str__(self):
		return self.description


class Comfort(models.Model):
	item = models.CharField(max_length=100)
	entry_date = models.DateField()

	def __str__(self):
		return self.item

class ExperienceWith(models.Model):
	entry = models.CharField(max_length=100)
	entry_date = models.DateField()

	def __str__(self):
		return self.entry

class PortfolioGraphic(models.Model):
	site_name = models.CharField(max_length=100)
	graphic = models.ImageField(storage = fs)
	site_url = models.URLField(max_length=100)
	upload_date = models.DateTimeField()

	def __str__(self):
		return self.graphic.url

class CarouselCover(models.Model):
	cover = models.ImageField(upload_to ='backgrounds')
	upload_date = models.DateTimeField()
	displayed = models.BooleanField()

	def __str__(self):
		return self.cover.url
