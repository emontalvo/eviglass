from django.urls import path

from . import views
## PARA IMPORTAR TODAS LAS VISTAS BASADAS EN CLASES ##
from .views import Empresa

urlpatterns = [
	path('', views.index, name = "inicio"),
	path('empresa/',Empresa.as_view(), name='empresa'),
]
