from django.urls import path

from .views import RegisterPersonal, PersonalList

urlpatterns = [

    path('users/personal/', RegisterPersonal.as_view(), name='novedades'),
    path('users/list_personal/', PersonalList.as_view(), name='PersonalList'),

]