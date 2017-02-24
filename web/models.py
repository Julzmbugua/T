from __future__ import unicode_literals

from django.db import models

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
	graphic = models.ImageField(upload_to = "portfolio")
	upload_date = models.DateTimeField()

	def __str__(self):
		return self.graphic.url

class CarouselCover(models.Model):
	cover = models.ImageField(upload_to = "homepage")
	upload_date = models.DateTimeField()

	def __str__(self):
		return self.cover.url
