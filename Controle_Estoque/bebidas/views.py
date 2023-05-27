from django.shortcuts import render
from django.contrib import messages

# Create your views here.
from datetime import date
from django.shortcuts import render, redirect
from .forms import BebidaForm, VendaForm
from .models import Bebidas, Venda


def index(request):

    users = Bebidas.objects.all()

    context = {
        'users': users
    }

    return render(request, 'index.html', context)


def cadastro(request):
    if request.method == 'GET':
        form = BebidaForm()
        context = {
            'form': form,
        }
        return render(request, 'cadastro.html', context=context)
    else:
        form = BebidaForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            if Bebidas.objects.filter(nome=nome).exists():
                messages.error(request, 'Já existe um produto com esse nome.')
                context = {'form': form}
                return render(request, 'cadastro.html', context=context)
            form.save()
            return redirect('index')
        else:
            messages.error(request, 'Ocorreu um erro no cadastro do produto.')
            context = {'form': form}
            return render(request, 'cadastro.html', context=context)
        
        
def refresh(request, user_id):

    user = Bebidas.objects.get(pk=user_id)

    if request.method == 'POST':
        form = BebidaForm(data=request.POST,instance=user)

        if form.is_valid():
            form.save()
            return redirect(index)
    else:
        form = BebidaForm(instance=user)

        context = {'form':form}

        return render(request,'cadastro.html', context=context)


def delete(request, user_id):

    user = Bebidas.objects.get(pk=user_id)
    user.delete()

    return redirect(index)

def sell(request):
    if request.method == 'POST':
        form = VendaForm(data=request.POST)

        if form.is_valid():
            nome = form.cleaned_data['nome']
            quantidade_vendida = form.cleaned_data['quantidade']

            if quantidade_vendida <= nome.quantidade:
                nome.quantidade -= quantidade_vendida
                nome.save()
                form.save()
                return redirect('index')
            else:
                form.add_error('quantidade', 'Quantidade insuficiente em estoque.')
                messages.error(request, 'Quantidade insuficiente em estoque.')
    else:
        form = VendaForm()

    context = {'form': form}

    return render(request, 'vendas.html', context=context)
