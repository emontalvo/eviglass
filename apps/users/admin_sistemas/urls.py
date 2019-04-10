from django.urls import path

from .views import RegisterPersonal, PersonalList, PersonalUpdate, PersonalDelete
from . import views

urlpatterns = [

    path('users/personal/', RegisterPersonal.as_view(), name='personal'),
    path('users/list_personal/', PersonalList.as_view(), name='PersonalList'),
    path('edit/<int:pk>', PersonalUpdate.as_view(), name='PersonalUpdate'),

    path('delete/<int:pk>', views.PersonalDelete.as_view(), name='PersonalDelete'),
    
    # path('delete/<id>/', views.delete, name='delete'),

]