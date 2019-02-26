from django.urls import path, include
from .views import (
    lista_bebidas,
    bebida_novo
)


urlpatterns = [
    path('', bebida_novo, name='core_lista_bebidas'),
    path('bebidas/',
     lista_bebidas,
      name='core_lista_bebidas'),
    path('bebida-novo', bebida_novo, name='core_bebida_novo')
]
