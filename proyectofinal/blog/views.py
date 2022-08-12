#from django.http import HttpResponse

# (Walter) Por ahora comento que la linea de arriba se puede eliminar porque
# en la linea de abajo, HttpResponse ya esta importado, por lo tanto
# es inecesaria, por ahora dejo el comentario para que se ubiquen, pero luego
# borramos todo esto.
# El que ve pone su nombre abajo y cuando todos lo vean borramos
#

from django.shortcuts import render, HttpResponse

# Create your views here.
def mi_vista(request):
    return render(request,"blog/index.html",{})