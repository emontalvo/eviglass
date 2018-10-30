from django.forms import ModelForm
from django import forms

from .models import Personal


class addPersForm(forms.ModelForm):
	nombre = forms.CharField(required=True)
	ci = forms.CharField(required=True)
	email = forms.EmailField(required=False)
	direccion = forms.CharField(required=True) 
	telefono = forms.IntegerField(required=True)
	cargo = forms.CharField(required=True)
	# password = forms.CharField(required=True)
	class Meta:
		model = Personal
		fields = ['nombre', 'ci', 'email', 'direccion', 'telefono', 'cargo']
