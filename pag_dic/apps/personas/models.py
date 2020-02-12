from django.db import models
from django.contrib.auth.models import User
from django.http import request
# Create your models here.

'''def get_user_id(request):
		username_logged=request.user.get_username()
		id_username= User.objects.get(username=username_logged)
		pk_user= id_username.id
		pk_user= int(pk_user)
		return pk_user'''


class Persona(models.Model):

	usuario_pk= models.ForeignKey(User, on_delete=models.CASCADE, default='1')
	nombre= models.CharField('Nombre', max_length=20)
	apellido= models.CharField('Apellido', max_length=20)
	email= models.EmailField('Email', blank=True)

	def __str__(self):
		return 'Id:{} Nombre:{} Apellido:{}'.format(self.id, self.nombre, self.apellido)
