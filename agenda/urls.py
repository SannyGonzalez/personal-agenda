from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='agenda'),
    path('crear', views.crear, name='crear_evento'),
    path('detalles/<int:id>', views.detalles, name='detalles_evento'),
    path('editar/<int:id>', views.editar, name='editar_evento'),
    path('borrar/<int:id>', views.borrar, name='borrar_evento')
]
