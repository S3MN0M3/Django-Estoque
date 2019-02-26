from django.forms import ModelForm
from .models import Estoque


class EstoqueForm(ModelForm):
    class Meta:
        model = Estoque
        fields = '__all__'

