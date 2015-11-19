"""PuntoVenta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sales/(?P<sale>([A-Z]{3,4}))/$', views.show_sale),
    """
    url(r'^altas/', views.altas),
    url(r'^patito/', views.patito),
    url(r'^carreras/$', views.lista_carreras, name="lista_carreras"),
    
    url(r'^carreras/agregar/$', views.agregar_carrera),
    url(r'^carreras/(?P<carrera>([A-Z]{3,4}))/editar/$', views.editar_carrera),
    url(r'^carreras/(?P<carrera>([A-Z]{3,4}))/eliminar/$', views.eliminar_carrera),
    url(r'^alumnos/$', views.lista_alumnos, name="lista_alumnos"),
    url(r'^alumnos/agregar/$', views.agregar_alumno),
    url(r'^alumnos/(?P<alumno>(\d{1,6}))/editar/$', views.editar_alumno),
    url(r'^alumnos/(?P<alumno>(\d{1,6}))/eliminar/$', views.eliminar_alumno),
    """
]
