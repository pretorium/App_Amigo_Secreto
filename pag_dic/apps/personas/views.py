from django.shortcuts import render
#__________________________________
from .models import Persona
#__________________________________
from django.views.generic import(
	ListView,
)

class lista_personas(ListView):
	template_name= 'personas/lista_personas.html'
	model= Persona
	context_object_name= 'personas'