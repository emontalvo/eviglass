from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.views.generic import TemplateView


# def index(request):
# 	return HttpResponse("holaaaa mundo")


def index(request):
	return render(request, 'inicio/inicio.html')

class Empresa(TemplateView):
	template_name = 'inicio/empresa.html'
	