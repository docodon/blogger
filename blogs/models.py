from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.
class Author(models.Model):
	user = models.OneToOneField(User)
	
	handle=models.CharField(max_length=30,primary_key=True)
	image=models.ImageField(null=True)
	
	def __str__(self):
		return "%s" %(self.user.username)



class Post(models.Model):
	title = models.CharField(max_length=64,unique=True)
	date = models.DateTimeField()
	author = models.ForeignKey(Author)
	body = models.TextField()
 	slug=models.SlugField()

 	def save(self,* args, **kwargs) :
		self.slug=slugify(self.title)
		super(Post,self).save(*args, **kwargs)

	def __str__(self):
		return "%s" % (self.title)