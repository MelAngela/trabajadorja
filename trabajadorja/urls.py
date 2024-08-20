"""
URL configuration for trabajadorja project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from solusoft import views
from django.views.generic import TemplateView  # Importa TemplateView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),  # Define la URL para la plantilla index.html
    path('trabajadores/', views.listar_trabajadores, name='listar_trabajadores'),
    path('trabajador/<int:trabajador_id>/', views.detalle_trabajador, name='detalle_trabajador'),
    path('trabajador/crear/', views.crear_trabajador, name='crear_trabajador'),
    path('trabajador/editar/<int:trabajador_id>/', views.editar_trabajador, name='editar_trabajador'),
    path('trabajador/buscar/', views.buscar_trabajador, name='buscar_trabajador'),
    path('trabajador/eliminar/<int:trabajador_id>/', views.eliminar_trabajador, name='eliminar_trabajador'),

    # URLs para Cargas
    path('trabajador/cargas/', views.listar_cargas, name='listar_cargas'),
    path('trabajador/<int:trabajador_id>/carga/agregar/', views.agregar_carga, name='agregar_carga'),
    path('trabajador/<int:trabajador_id>/carga/detalle/<int:carga_id>/', views.detalle_carga, name='detalle_carga'),
    path('trabajador/<int:trabajador_id>/carga/detalle/', views.detalle_carga, name='detalle_carga'),
    path('trabajador/<int:trabajador_id>/carga/editar/<int:carga_id>/', views.editar_carga, name='editar_carga'),
    path('trabajador/<int:trabajador_id>/carga/eliminar/<int:carga_id>/', views.eliminar_carga, name='eliminar_carga'),
    path('buscar_trabajador_cargas/', views.buscar_trabajador_cargas, name='buscar_trabajador_cargas'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)