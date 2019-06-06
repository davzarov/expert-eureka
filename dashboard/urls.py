from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('ingresar', views.login_request, name='ingresar'),
    path('salir', views.logout_request, name='salir'),
    path('cambiar-contrasena', views.change_password, name='cambiar_contraseña'),
]
