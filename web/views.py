from django.shortcuts import render
from django.http import HttpResponse
from .models import About, CarouselCaption, Comfort, PortfolioGraphic,\
 ExperienceWith, CarouselCover

# Create your views here.
def homepage(request):
	# Home
	# cover_img = CarouselCover.objects.order_by('upload_date')[0]
	caption_item = CarouselCaption.objects.order_by('publish_date')[0]
	caption_item_1 = CarouselCaption.objects.order_by('publish_date')[1]
	caption_item_2 = CarouselCaption.objects.order_by('publish_date')[2]

	#About
	bio_desc = About.objects.order_by('publish_date')[1]

	#Resume
	comfort_item = Comfort.objects.all()
	experience_list = ExperienceWith.objects.all()

	# Portfolio
	graphic_item = PortfolioGraphic.objects.order_by('upload_date')[0]
	graphic_item_1 = PortfolioGraphic.objects.order_by('upload_date')[1]
	graphic_item_2 = PortfolioGraphic.objects.order_by('upload_date')[2]

	context = {
		'caption_item': caption_item,
		'caption_item_1': caption_item_1,
		'caption_item_2': caption_item_2,
		'bio_desc':bio_desc,
		'comfort_item': comfort_item,
		'graphic_item': graphic_item,
		'graphic_item_1': graphic_item_1,
		'graphic_item_2': graphic_item_2,
		'experience_list': experience_list
		}
	return render(request, 'layout.html', context)
	