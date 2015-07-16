from django.db import models
from django.contrib.auth.models import User

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
 	
	def __str__(self):
		return "%s" % (self.title)