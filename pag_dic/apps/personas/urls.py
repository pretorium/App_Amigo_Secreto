from django.urls import path, re_path
from django.contrib.auth.decorators import login_required #<--- Restringir las vistas a usuarios
#____________________________________
from apps.personas.views import(
	lista_personas,
	registrar_persona,
	eliminar_persona,
	sorteo,
	editar_persona,
)
#____________________________________
app_name= 'personas_app'

urlpatterns= [
	path('', lista_personas.as_view(), name='lista_personas'),
	path('inscribir/', login_required(registrar_persona.as_view()), name='registrar_persona'),
	path('eliminar/<pk>/', login_required(eliminar_persona.as_view()), name='eliminar_persona'),
	path('editar/<int:pk>/', login_required(editar_persona.as_view()), name= 'editar_persona'),
	path('sortear/', login_required(sorteo), name='sorteo'),
]