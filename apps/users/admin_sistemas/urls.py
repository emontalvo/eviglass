from django.urls import path

from .views import RegisterPersonal, PersonalList
from . import views

urlpatterns = [

    path('users/personal/', RegisterPersonal.as_view(), name='personal'),
    path('users/list_personal/', PersonalList.as_view(), name='PersonalList'),
    
    path('delete/<id>/', views.delete, name='delete'),

]