from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.urls import reverse_lazy
# Create your views here.
from apps.usuarios.forms import formato_usuario

class registrar_usuario(CreateView):
	models= User
	template_name= 'usuarios/registrar_usuario.html'
	form_class= formato_usuario
	success_url= reverse_lazy('personas_app:lista_personas')