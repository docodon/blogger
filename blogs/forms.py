from django.db import models
from django import forms
from blogs.models import Author,Post
from django.contrib.auth.models import User


class BLOGENTRY(forms.Form):
	title=forms.CharField()
	blog=forms.CharField(widget=forms.Textarea)

	
class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model=User
		fields=('first_name','last_name','email','username','password')

class ExtraInfo(forms.Form):
	image=forms.ImageField()