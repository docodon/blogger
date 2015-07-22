import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','blogger.settings')

import django
from django.template.defaultfilters import slugify

django.setup()

from blogs.models import Post,Author

def add_blog(body,title) :
	p=Post.objects.get_or_create(title=title,body=body)[0]
	#print p
	p.slug=slugify(title)
	p.save();

if __name__=='__main__':
	for i in Post.objects.all() :
		add_blog(i.body,i.title)
