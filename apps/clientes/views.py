from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

#configuração api asaas
from formare.settings import ASAAS_API_KEY, ASAAS_API_URL
import requests
import json
import urlopen

# Create your views here.
from .forms import ClienteForm
from .models import Cliente

def get_headers():
    headers = {
        'Content-Type': 'application/json',
        'access_token': ASAAS_API_KEY
    }
    return headers

id_cliente=1

def create_customer(api_key='',id_cliente=id_cliente):
    
    url = ASAAS_API_URL + '/customers'
    headers = get_headers()
    cliente = Cliente.objects.get(id=id_cliente)
    JSON = {
        'name': cliente.name,
        'cpfCnpj': cliente.cpfCnpj,
        'email': cliente.email,
        'mobilePhone': cliente.mobilePhone,
        'postalCode': cliente.postalCode,
        'addressNumber': cliente.addressNumber
    }
    response = requests.post(url, data=json.dumps(JSON), headers=headers)
    print(f'status_code: {response.status_code}, content: {response.content}')
    return {'status_code': response.status_code, 'content': response.content}

def cadastro_cliente(request):
    form = ClienteForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            id_cliente = f.id 
            create_customer(api_key='',id_cliente=id_cliente)
            return redirect(request.GET.get('next','/cliente/matricula/concluida/'))
        else:
            print(form.errors)
            messages.error(request, form.errors)
            form = ClienteForm()
    return render(request,'clientes/pre_cadastro.html',{'form':form})

def matricula_concluida(request):
    return render(request,'clientes/concluido.html',{})