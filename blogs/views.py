from django.shortcuts import render
from blogs.models import Post,Author
from django.contrib.auth.models import User
from blogs.forms import BLOGENTRY,UserForm,ExtraInfo
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login , logout
from django.db import IntegrityError

def index(request) :
	
	all_posts=Post.objects.all().order_by('-date')
	template_data={'posts':all_posts}

	return render(request,'index.html',template_data)


@login_required()
def add_blog(request) :
	
	if request.method=='POST':
		form=BLOGENTRY(request.POST)
		if form.is_valid() :
			form=form.cleaned_data
			A=Post(title=form['title'],body=form['blog'],date=timezone.now(),author=Author.objects.get(handle=request.user.username))
			try :
				A.save()
			except IntegrityError as e:
				return render(request,'add_blog.html',{'form':BLOGENTRY(),'error':e.message})
			return index(request)
		else :
			return render(request,'add_blog.html',{'form':BLOGENTRY(),'error':'something went wrong..'})
	else :
		return render(request,'add_blog.html',{'form':BLOGENTRY()})



def register(request):
	error=dict()
	if request.user.username != '' :
		return logout_user(request)
	

	if request.method=='POST' :
		form=UserForm(request.POST)
		form2=ExtraInfo(request.POST)
		if form.is_valid() :
			u=form.save()
			u.set_password(form.cleaned_data['password'])
			u.save()
			if 'image' in request.FILES :
				p=Author.objects.create(user=u,handle=form.cleaned_data['username'],image=request.FILES['image'])
			else :		
				p=Author.objects.create(user=u,handle=form.cleaned_data['username'])
			return index(request)
		else :
			error='Cant create the account please see your information entered is valid'
	return render(request,'blogs/registration.html',{'form':UserForm(),'error':error,'form2':ExtraInfo()}) ;	


def login_user(request) :
	if request.user.username != '' :
		return logout(request)
	
	error=dict()
	if request.method=='POST' :
		user=authenticate(username=request.POST['handle'] , password=request.POST['password'])
		if user :
			if user.is_active :
				login(request,user)
				return index(request) 
			else :
				error['error']="This account is deactivated ."
		else :
			error['error']="Account details not matched enter your details again !"
		
	return render(request,'login.html',error)



@login_required()
def logout_user(request) :
	logout(request)
	return index(request)


def search_user(request) :
	if request.method=="GET" :
		aut=Author.objects.filter(handle=request.GET['handle'])
		if not aut :
			return render(request,'index.html',{'error':'no such user found . please check your handle !'})
		return profile_view(request,aut[0].handle)

		detail={'handle':aut.handle,'name':aut.user.first_name+aut.user.last_name,'email':aut.user.email}
		detail['blogs']=Post.objects.filter(author=aut)
		print 'here'
		return render(request,'profile_view.html',detail)


		
def profile_view(request,aut) :
	if aut :
		ret=Author.objects.get(handle=aut)
		detail={'handle':ret.handle,'name':ret.user.first_name+'  '+ret.user.last_name,'email':ret.user.email,}
		if ret.image :
			detail['image']=ret.image
		blg=Post.objects.filter(author=ret)
		blog=dict()
		for i in blg :
			blog[i.title]=i.body
		detail['blogs']=blg
		return render(request,'profile_view.html',detail)