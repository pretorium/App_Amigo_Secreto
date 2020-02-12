from django import forms
from apps.personas.models import Persona

class persona_form(forms.ModelForm):

	class Meta:
		model= Persona

		fields= [
			'nombre',
			'apellido',
			'email'
		]

		labels= {
			'nombre': 'Nombre',
			'apellido': 'Apellido',
			'email': 'Email'
		}

		widgets= {
			'nombre': forms.TextInput(attrs={'class': 'form-control'}),
			'apellido': forms.TextInput(attrs={'class': 'form-control'}),
			'email': forms.TextInput(attrs={'class': 'form-control'}),
		}