from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import *
from .forms import *

# Create your views here.
def homepage(request):
	# Home
	cover_img = CarouselCover.objects.get(slide = 0)	
	cover_img_1 = CarouselCover.objects.get(slide = 1)
	cover_img_2	 = CarouselCover.objects.get(slide = 2)
	caption_item = CarouselCaption.objects.get(caption_no = 1)
	caption_item_1 = CarouselCaption.objects.get(caption_no = 2)
	caption_item_2 = CarouselCaption.objects.get(caption_no = 3)
	caption_item_3 = CarouselCaption.objects.get(caption_no = 4)


	#About
	bio_desc = About.objects.order_by('publish_date')[0]

	#Resume
	comfort_item = Comfort.objects.all()
	experience_list = ExperienceWith.objects.all()

	# Portfolio
	graphic_item = PortfolioGraphic.objects.get(graphic_no = 0)
	graphic_item_1 = PortfolioGraphic.objects.get(graphic_no = 1)
	graphic_item_2 = PortfolioGraphic.objects.get(graphic_no = 2)


	context = {
		'cover_img':cover_img,
		'cover_img_1':cover_img_1,
		'cover_img_2':cover_img_2,
		'caption_item': caption_item,
		'caption_item_1': caption_item_1,
		'caption_item_2': caption_item_2,
		'caption_item_3': caption_item_3,
		'bio_desc':bio_desc,
		'comfort_item': comfort_item,
		'graphic_item': graphic_item,
		'graphic_item_1': graphic_item_1,
		'graphic_item_2': graphic_item_2,
		'experience_list': experience_list
		}
	return render(request, 'layout.html', context)
	
class BlogCreate(CreateView):
	model = Blog
	fields = ['blog_title', 'blog_content', 'publish_date']	



class BlogUpdate(CreateView):
	model = Blog
	fields = ['blog_title', 'blog_content', 'publish_date']	


class BlogDelete(DeleteView):
	model = Blog
	# fields = ['blog_title', 'Blog_content', 'publish_date']	
	sucess_url = reverse_lazy('web:homepage')

