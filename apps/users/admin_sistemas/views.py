from django.shortcuts import render, redirect

# Create your views here.


from django.views.generic import FormView, CreateView, ListView, UpdateView, DeleteView
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
		# print RegisterPersonal.id
		return super(RegisterPersonal, self).form_valid(form)

class PersonalList(ListView):
	template_name= 'users/admin_sistemas/list_personal.html'
	context_object_name = 'personal'
	queryset = Personal.objects.all()

# class PersonalUpdate(UpdateView):
# 	template_name = 'users/admin_sistemas/update_personal.html'
# 	# form_class = addPersForm
# 	model = Personal
# 	fields = ['nombre','ci','email','direccion','telefono','cargo']	
# 	success_url = '/users/list_personal/'


class PersonalUpdate(UpdateView):
    
    model = Personal
    form_class = addPersForm
    template_name = 'users/admin_sistemas/update_personal.html'
    success_url = '/users/list_personal/'

# def edit(request, id):
# 	lista_pers = Personal.objects.get(pk=id)
# 	context = {
# 		lista_pers : lista_pers
# 	}
# 	return render(request, 'edit.html', context)


class PersonalDelete(DeleteView):
	template_name = 'users/admin_sistemas/personal_confirm_delete.html'
	model = Personal
	success_url = '/users/list_personal/'

# def delete(request, id):
# 	lista_pers = Personal.objects.get(pk=id)
# 	lista_pers.delete()
# 	return redirect('/users/list_personal/')



