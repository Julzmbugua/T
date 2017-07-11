from django.forms import ModelForm
from .models import *

class BlogForm(ModelForm):
	class Meta:
		model = Blog
		fields = [
		'blog_title',
		'blog_content',
		'publish_date'
		]



# class BlogForm(forms.Form):
#     blog_title = forms.CharField(label='Blog Title', max_length=100)
#     blog_content = forms.TextField(label = 'What is on your mind?', max_length=1000)
#     publish_date = forms.DateTimeField()
    

