from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from . import views

app_name = 'web'

urlpatterns = [

	url(r'^$', views.homepage, name='homepage'),
	# url(r'^portfolio/$', views.portfolio, name='portfolio'),
	# url(r'^about/$', views.about, name='about'),
	# url(r'^resume/$', views.resume, name='resume'),	
	url(r'^blog/$', views.BlogCreate.as_view(), name='blog-add')
	# url(r'^contact/$', views.contact, name='contact'),
] 

