
from django.urls import path , include
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('formulario/', views.Solicitud , name='formulario'),
    path('internet/',  views.internet , name='internet'),
    path('movil/',  views.movil , name='movil'),
    path('telefonia/',  views.telefonia, name='telefonia'), 
]
