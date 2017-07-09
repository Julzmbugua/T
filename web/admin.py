from django.contrib import admin
from .models import *


# Register your models here.
class CarouselCaptionAdmin(admin.ModelAdmin):
	list_display = ('caption', 'caption_no', 'publish_date')		

class PortfolioGraphicAdmin(admin.ModelAdmin):
	list_display = ('site_name', 'site_url', 'graphic', 'upload_date')		

class CarouselCoverAdmin(admin.ModelAdmin):
	list_display = ('upload_date', 'displayed')


admin.site.register(CarouselCaption, CarouselCaptionAdmin)
admin.site.register(About)
admin.site.register(Comfort)
admin.site.register(ExperienceWith)
admin.site.register(PortfolioGraphic, PortfolioGraphicAdmin)
admin.site.register(CarouselCover, CarouselCoverAdmin)

# Register your models here.

