from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='contactos'),
    path('crear/', views.crear, name='crear_contacto'),
    path('detalles/<int:id>', views.detalles, name='detalles_contacto'),
    path('editar/<int:id>', views.editar, name='editar_contacto'),
    path('borrar/<int:id>', views.borrar, name='borrar_contacto'),
]

