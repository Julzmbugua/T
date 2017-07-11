from __future__ import unicode_literals

from django.db import models
from django.core.files.storage import FileSystemStorage


fs = FileSystemStorage(location='web/media/')

# Create your models here.
class CarouselCaption(models.Model):
	caption = models.CharField(max_length=100)
	publish_date = models.DateField()
	caption_no = models.IntegerField()

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
	graphic_no = models.IntegerField(unique=True)
	upload_date = models.DateTimeField()

	def __str__(self):
		return self.graphic.url

class CarouselCover(models.Model):
	alt = models.CharField(max_length=10)
	cover = models.ImageField(upload_to ='backgrounds')
	upload_date = models.DateTimeField()
	slide = models.IntegerField()

	def __str__(self):
		return self.cover.url
class Blog(models.Model):
    blog_title = models.CharField(max_length=100)
    blog_content = models.TextField(max_length=1000)
    publish_date = models.DateTimeField()
    def __str__(self):
		return self.blog_title + '-' + self.blog_contentl
    
    def get_absolute_url(self):
    	return reverse('web:blog', kwargs={'pk:self.pk'})