from django.contrib import admin
from .models import *
from django_markdown.admin import MarkdownModelAdmin
from django_markdown.widgets import AdminMarkdownWidget




# Register your models here.
class CarouselCaptionAdmin(admin.ModelAdmin):
	list_display = ('caption', 'caption_no', 'publish_date')		

class PortfolioGraphicAdmin(admin.ModelAdmin):
	list_display = ('site_name', 'site_url', 'graphic', 'graphic_no', 'upload_date')		

class CarouselCoverAdmin(admin.ModelAdmin):
	list_display = ('alt', 'upload_date', 'slide')

class BlogAdmin(MarkdownModelAdmin):
	list_display = ('blog_title', 'blog_content','created')
	prepopulated_fields = {'slug': ('blog_title',)}


admin.site.register(CarouselCaption, CarouselCaptionAdmin)
admin.site.register(About)
admin.site.register(Comfort)
admin.site.register(ExperienceWith)
admin.site.register(PortfolioGraphic, PortfolioGraphicAdmin)
admin.site.register(CarouselCover, CarouselCoverAdmin)
admin.site.register(Blog, BlogAdmin)

# Register your models here.

