from django.db import models

# Create your models here.

class Personal(models.Model):

	nombre = models.CharField(max_length=100)
	ci = models.CharField(max_length=100)
	email = models.EmailField()
	direccion = models.CharField(max_length=100) 
	telefono = models.IntegerField()
	cargo = models.CharField(max_length=100)
	fechaCreacion = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __str__(self):
		return self.nombre

	def get_absolute_url(self):
		return reverse('personal_edit', kwargs={'pk': self.pk})