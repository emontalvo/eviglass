from django.urls import path, include

from . import views
## PARA IMPORTAR TODAS LAS VISTAS BASADAS EN CLASES ##
from .views import Novedades, Ofertas, Contactos, QuienesSomos

urlpatterns = [
	path('Portal/', views.index, name = "inicio"),
	# path('empresa/',Empresa.as_view(), name='empresa'),
	path('quienessomos/' ,QuienesSomos.as_view(), name='quienessomos'),
	path('novedades/', Novedades.as_view(), name='novedades'),
	path('ofertas/', Ofertas.as_view(), name='ofertas'),
	path('contactos/', Contactos.as_view(), name='contactos'),


	path('accounts/', include('django.contrib.auth.urls'))

	



]
