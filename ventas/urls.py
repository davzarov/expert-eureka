from django.urls import path
from . import views

app_name = 'ventas'

urlpatterns = [
    path('pos', views.pos, name='pos'),
]
