from django.shortcuts import render_to_response
from plants.models import Plantkind, Plant
# Create your views here.
# -*-coding: uth-8 -*-
def plantlist(request):
	plants = Plant.objects.all()
	kinds = Plantkind.objects.all()

	return render_to_response('plant.html',locals())


def plant1(request):

	return render_to_response('七福神圖鑑詳細資料.html',locals())

def plant2(request):

	return render_to_response('月兔耳圖鑑詳細資料.html',locals())

def plant3(request):

	return render_to_response('玉露圖鑑詳細資料.html',locals())

def plant4(request):

	return render_to_response('生石花圖鑑詳細資料.html',locals())

def plant5(request):

	return render_to_response('白鳳菊圖鑑詳細資料.html',locals())

def plant6(request):

	return render_to_response('星兜圖鑑詳細資料.html',locals())

def plant7(request):

	return render_to_response('虹之玉圖鑑詳細資料.html',locals())

def plant8(request):

	return render_to_response('姬星美人圖鑑詳細資料.html',locals())

def plant9(request):

	return render_to_response('球松圖鑑詳細資料.html',locals())

def plant10(request):

	return render_to_response('雪蓮圖鑑詳細資料.html',locals())

def plant11(request):

	return render_to_response('碧光環圖鑑詳細資料.html',locals())

def plant12(request):

	return render_to_response('月兔耳圖鑑詳細資料.html',locals())

def plant13(request):

	return render_to_response('錦上珠圖鑑詳細資料.html',locals())

def plant14(request):

	return render_to_response('露娜蓮圖鑑詳細資料.html',locals())

def plant15(request):

	return render_to_response('鷹爪圖鑑詳細資料.html',locals())
