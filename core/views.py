from django.shortcuts import render, redirect
from .models import Estoque, Bebida
from .forms import EstoqueForm


def lista_bebidas(request):
    bebidas = Bebida.objects.all()
    estoques = Estoque.objects.all()
    form = EstoqueForm()
    data = {'bebidas': bebidas, 'form': form, 'estoques': estoques}
    return render(request, 'core/lista_bebidas.html', data)


def bebida_novo(request):
    form = EstoqueForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_bebidas')
