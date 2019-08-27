from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.views.generic import TemplateView, ListView

# from apps.users.admin_sistemas.models import ReqistrarProducto


# def index(request):
# 	return HttpResponse("holaaaa mundo")


def index(request):
	return render(request, 'inicio/inicio.html')

# class Empresa(TemplateView):
# 	template_name = 'inicio/empresa.html'






class QuienesSomos(TemplateView):
	template_name = 'inicio/quienessomos.html'


class Novedades(TemplateView):
	# context_object_name = "producto"
	# queryset = RegistrarProducto.objects.filter(webnovedad='true')[0:5]
	template_name = 'inicio/novedades.html'

class Ofertas(TemplateView):
	# context_object_name = "producto"
	# queryset = RegistrarProducto.objects.filter(weboferta='true')[0:5]
	template_name = 'inicio/ofertas.html'

class Contactos(TemplateView):

	template_name = 'inicio/contactos.html'

