from django.conf.urls import url
from apps.usuarios.views import registrar_usuario

app_name= 'usuarios_app'

urlpatterns=[
	url('registrar/', registrar_usuario.as_view(), name='registrar')
	]
	