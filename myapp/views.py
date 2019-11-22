import requests
from myapp.models import Webcontent
from django.http import HttpResponse
from django.shortcuts import render


def home(request) :
     #return HttpResponse('<h1>hello</h1>')

    webcontentToSave = Webcontent(
      webTextContent = "www.polo.com"
    )
   
    webcontentToSave.save()
    
    
    objects = Webcontent.objects.all()
   
    for elt in objects:
        res = elt.webTextContent
        print(res)
    
    
    return render(request,'myapp/index.html')

def blog(request) :
    return render(request,'myapp/blog.html')

def single_blog(request) :
    return render(request,'myapp/single-blog.html')

def contact(request) :
    return render(request,'myapp/contact.html')

def event(request) :
    return render(request,'myapp/event.html')

def elements(request) :
    return render(request,'myapp/elements.html')

def causes(request) :
    return render(request,'myapp/causes.html')

def about(request) :
    return render(request,'myapp/about.html')
