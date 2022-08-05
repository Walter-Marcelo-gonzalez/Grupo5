from django.http import HttpResponse
from django.shortcuts import render, HttpResponse

# Create your views here.
def mi_vista(request):
    return HttpResponse('<h1>Grupo 5 <h1>')