from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from myapp.models import *
# Create your views here.
def hello(request):
	msg="welcome django"
	return HttpResponse(msg)

def hi(request):
	msg="<h1>Django App</h1>"
	msg=msg+"<h2>Hello</h2>"
	return HttpResponse(msg)

def mygoogle(request):
	return redirect('http://www.google.com')

def welcome(request,name):
	msg="welcome dear"+name
	return HttpResponse(msg)

def index(request):
	return render(request,'index.html')

def agra(request):
	return render(request,'agra.html')

def forminput(request):
	return render(request,'forminput.html')

@csrf_exempt
def login(request):
	a=request.POST.get("sname")
	b=request.POST.get("spass")
	if a=="test" and b =="123":
		return render(request,'success.html')
	else:
		return render(request,'failed.html')

def success(request):
	return render(request,'success.html')

def failed(request):
	return render(request,'failed.html')

def stinput(request):
	return render(request,'stinput.html')

@csrf_exempt
def stsave(request):
	a=request.POST.get("sname")
	b=request.POST.get("scity")
	d=request.POST.get("semail")
	obj=Student(name=a,city=b,email=d)
	obj.save()
	return HttpResponse("Saved")

def stshow(request):
	obj=Student.objects.all()
	msg="<h1>Data is</h1>"
	for res in obj:
		msg=msg+res.name+"<br>"
		msg=msg+res.city+"<br>"
		msg=msg+res.email+"<br>"
	return HttpResponse(msg)

def stfind(request):
	return render(request,'stfind.html')

@csrf_exempt
def searchdata(request):
	a=request.POST.get("sname")
	obj=Student.objects.filter(name=a)
	msg="<h1>Data is</h1>"
	
	for res in obj:
		msg=msg+res.name+"<br>"
		msg=msg+res.city+"<br>"
		msg=msg+res.email+"<br>"
	return HttpResponse(msg)

def stdel(request):
	return render(request,'stdel.html')

@csrf_exempt
def deletedata(request):
	a=request.POST.get("sname")
	obj=Student.objects.get(name=a)
	obj.delete()
	return HttpResponse("Deleted")

def revised(request):
	return render(request,'revised.html')

def python(request):
	return render(request,'python.html')
	


