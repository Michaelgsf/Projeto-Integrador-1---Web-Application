from django import forms
from .models import Bebida

# modelForm


class BebidaForm(forms.ModelForm):
    class Meta:
        model = Bebida
        fields = ['nome', 'quantidade', 'preco']


# form.Form