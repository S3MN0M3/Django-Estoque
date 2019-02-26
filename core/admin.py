from django.contrib import admin
from .models import (
    Bebida, Estoque
)


class EstoqueAdmin(admin.ModelAdmin):
    list_display = (
        'marca', 'quantidade', 'data', 'entrada', 'saida')


admin.site.register(Bebida)
admin.site.register(Estoque, EstoqueAdmin)