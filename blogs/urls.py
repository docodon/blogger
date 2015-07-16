from django.conf.urls import patterns, include, url
from django.contrib import admin
from blogs import views

urlpatterns = patterns('',
    url(r'^list/$',views.index,name='index'),
    url(r'^add_blog/$',views.add_blog,name='add_blog'),
    url(r'^register/$',views.register,name='register'),
    url(r'^login/$',views.login_user,name='login'),
    url(r'^logout/$',views.logout_user,name='logout'),
    url(r'^search/$',views.search_user,name='search'),
    url(r'^profile/$',views.profile_view,name='profile')
)

