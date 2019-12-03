from django.urls import path, re_path
#____________________________________
from apps.personas.views import(
	lista_personas,
)
#____________________________________
app_name= 'personas_app'

urlpatterns= [
	path('', lista_personas.as_view(), name='lista_personas')
]