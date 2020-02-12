from django.shortcuts import render
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.http import HttpResponse, request
from django.contrib.auth.models import User
import random
#__________________________________
from .models import Persona
from .forms import persona_form
#__________________________________
from django.views.generic import(
	ListView,
	CreateView,
	DeleteView,
	TemplateView,
	UpdateView,
)


class lista_personas(ListView):
	template_name= 'personas/lista_personas.html'
	model= Persona
	context_object_name= 'personas'

class registrar_persona(CreateView):
	template_name= 'personas/registrar_personas.html'
	model= Persona
	form_class= persona_form
	success_url= reverse_lazy('personas_app:lista_personas')

class eliminar_persona(DeleteView):
	model= Persona
	template_name= 'personas/eliminar_personas.html'
	success_url= reverse_lazy('personas_app:lista_personas')

class editar_persona(UpdateView):
	model= Persona
	template_name= 'personas/editar_persona.html'
	form_class= persona_form
	success_url= reverse_lazy('personas_app:lista_personas')

def sorteo(request):
	#prueba id
	''''username_logged=request.user.get_username()
				id_username= User.objects.get(username=username_logged)
				pk_user= id_username.id
				print (pk_user)
    #prueba de obtener el id del user logueado
	current_user = request.user
				print (f'Id del Usuario logged: {current_user.id}')'''
	
	#__________________________________________________
	#peronas= Persona.objects.all()
	#pks= list(personas)

	#random.shuffle(pks)
	#pks.append(pks[0])
			
	#for p in range(len(pks) - 1):
		#e=Persona.objects.get(pk=str(pks[p]))
		#n=Persona.objects.get(pk=str(pks[p + 1]))

		#print(f'{e.email} ---> {n.nombre}')
		
		#send_mail('Tu amigo secretro [ENSAYO]!',
			#f'Tu AMIGO SECRETO [ENSAYO] para este intercambio navideño es: {n.nombre}!',
			#'amigo.secreto.dic2019@gmail.com',
			#[f'{e.email}'],)
		#print('enviado!')
	#________________________________________________________________________________________
	return render(request, 'sorteo/sorteo.html')

def get_user_id(request):
	username_logged=request.user.get_username()
	id_username= User.objects.get(username=username_logged)
	pk_user= id_username.id
	return pk_user
