from django.db import models

# Create your models here.

class Persona(models.Model):
	nombre= models.CharField('Nombre', max_length=20)
	apellido= models.CharField('Apellido', max_length=20)

	def _str__(self):
		return self.nombre.apellido

	