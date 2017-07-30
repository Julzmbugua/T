from __future__ import unicode_literals
import datetime
from django.urls import reverse
from django.db import models
from django.core.files.storage import FileSystemStorage
from django_markdown.models import MarkdownField


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

class BlogQuerySet(models.QuerySet):
	def published(self):
		return self.filter(publish=True)
class Blog(models.Model):
    blog_title = models.CharField(max_length=100)
    blog_content = MarkdownField()
    slug = models.SlugField(max_length=200, unique=True)
    publish = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    objects = BlogQuerySet.as_manager()

    def __str__(self):
		return self.blog_title + '-' + self.blog_content
    class Meta:
        verbose_name = "Blog Entry"
        verbose_name_plural = "Blog Entries"
        ordering = ["-created"]
    def get_absolute_url(self):
    	return reverse('web:blog-detail', kwargs={'pk':self.pk})
