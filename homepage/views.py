from django.shortcuts import render_to_response

# Create your views here.
# -*-coding: uth-8 -*-
def home(request):
	return render_to_response('homepage.html',locals())

def link(request):
	return render_to_response('link.html',locals())

def photo(request):
	return render_to_response('photo.html',locals())

def introduce(request):
	return render_to_response('introduce.html',locals())

def newbie(request):
	return render_to_response('newbie.html',locals())