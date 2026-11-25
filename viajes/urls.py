from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("destinos/", views.destinos, name="destinos"),
    path("nosotros/", views.nosotros, name="nosotros"),
    path("servicios/", views.servicios, name="servicios"),
    path("contacto/", views.contacto, name="contacto"),
]