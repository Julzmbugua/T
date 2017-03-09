from django.conf.urls import include, url
from . import views

app_name = 'web'

urlpatterns = [

	url(r'^$', views.homepage, name='homepage'),
	# url(r'^portfolio/$', views.portfolio, name='portfolio'),
	# url(r'^about/$', views.about_page, name='about_page'),
	# url(r'^resume/$', views.resume, name='resume'),
	# url(r'^blog/$', views.blog, name='blog'),
	# url(r'^contact/$', views.contact, name='contact'),
]

