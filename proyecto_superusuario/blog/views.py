from django.shortcuts import render,HttpResponse

# Create your views here.

def mi_vista(request):
	return render(request,"blog/practica1.html",{})
