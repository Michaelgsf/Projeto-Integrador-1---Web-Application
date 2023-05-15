from django.shortcuts import render

# Create your views here.
from datetime import date
from django.shortcuts import render, redirect
from .forms import BebidaForm
from .models import Bebida


def index(request):

    users = Bebida.objects.all()

    context = {
        'users': users
    }

    return render(request, 'index.html', context)


def create(request):

    # GET
    # POST
    # PUT
    # DELETE

    if request.method == 'GET':
        form = BebidaForm()
        # muito importante essa barte abaixo

        context = {
            'form': form,
        }
        return render(request, 'cadastro.html', context=context)
    else:
        form = BebidaForm(request.POST)
        if form.is_valid():
            form.save()
            """- usados pra salvar sem a pagina dinámica"""
            return redirect(index)


def refresh(request, user_id):

    user = Bebida.objects.get(pk=user_id)

    if request.method == 'POST':
        form = BebidaForm(data=request.POST,instance=user)

        if form.is_valid():
            return redirect(index)
    else:
        form = BebidaForm(instance=user)

        context = {'form':form}

        return render(request,'cadastro.html', context=context)


def delete(request, user_id):

    user = Bebida.objects.get(pk=user_id)
    user.delete()

    return redirect(index)


