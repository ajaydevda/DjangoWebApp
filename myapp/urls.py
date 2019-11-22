from django.contrib import admin
from django.urls import path
from django.conf.urls import url 
from . import views


urlpatterns = [
    path('', views.home ),
   # url(r'blog', views.blog,name='blog'),
    path('index', views.home, name='index'),

    path('blog', views.blog, name='blog'),
    path('blog', views.single_blog, name='single_blog_page'),
    path('contact', views.contact, name='contact'),
    path('event', views.event, name='event'),
    path('elements', views.elements, name='elements'),
    path('causes', views.causes, name='causes'),
    path('about', views.about, name='about'),

]
