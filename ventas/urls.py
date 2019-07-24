from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.generic import TemplateView

app_name = 'ventas'

urlpatterns = [
    path('', login_required(TemplateView.as_view(template_name='ventas/pos.html')), name='pos')
]
