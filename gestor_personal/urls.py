from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contactos/', include('contactos.urls')),
    path('agenda/', include('agenda.urls')),
    path('', views.index, name='index')
]
