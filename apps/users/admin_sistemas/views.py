from django.shortcuts import render

# Create your views here.


from django.views.generic import FormView, CreateView, ListView
from .models import Personal
from .forms import addPersForm

class RegisterPersonal(FormView):
	template_name = "users/admin_sistemas/personal_form.html"
	# fields = ('nombre', 'apellido')
	form_class= addPersForm
	success_url = '/users/list_personal/'

	def form_valid(self, form):

		regPersonal = Personal()
		regPersonal.nombre = form.cleaned_data['nombre']
		regPersonal.ci = form.cleaned_data['ci']
		regPersonal.email = form.cleaned_data['email']
		regPersonal.direccion = form.cleaned_data['direccion']
		regPersonal.telefono = form.cleaned_data['telefono']
		regPersonal.cargo = form.cleaned_data['cargo']
		regPersonal.save()
		# print registrarPersonal.id
		return super(RegisterPersonal, self).form_valid(form)

class PersonalList(ListView):
	template_name= 'users/admin_sistemas/list_personal.html'
	context_object_name = 'personal'
	queryset = Personal.objects.all()
