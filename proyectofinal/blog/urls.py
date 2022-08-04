from django.urls import path
from . import views

urlpattern = [
    path('', views.mi_vista, name='mi_vista'),
]