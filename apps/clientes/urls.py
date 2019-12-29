from django.urls import path,include
from . import views


app_name='clientes'
urlpatterns = [
    path('cadastro/2020/',views.cadastro_cliente),
]