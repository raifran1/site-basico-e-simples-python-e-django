from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request,'site/index.html',{})

def sitemap(request):
    return render(request,'core/sitemap.xml',{})

def contato(request):
    return render(request,'site/contact.html',{})