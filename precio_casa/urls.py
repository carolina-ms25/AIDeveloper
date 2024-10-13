from django.urls import path
from . import views

urlpatterns = [
    path("estimar/",views.estimar_precio_casa,name="estimar_precio_casa")
    ]
