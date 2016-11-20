from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from sitmoduloregistro.quickstart.serializers import UserSerializer, GroupSerializer
import json
import textwrap
from django.http import HttpResponse
from django.http import JsonResponse

from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from models import *
from rest_framework.permissions import IsAuthenticated

class UserForm(ModelForm):
    class Meta:
        model = AuthUser
        fields = "__all__"

def user_list(request, template_name='users/user_list.html'):
    return JsonResponse({'Status': 'Failed', 'Message' : 'Access Denied'})

@api_view(['POST'])
def user_create(request):
    if request.method == 'POST':
        nu = request.body;
        nu = json.loads(nu)
        user = AuthUser()
        user.password = nu['password']
        user.first_name = nu['first_name']
        user.last_name = nu['last_name']
        user.email = nu['email']
        user.username = nu['username']
        user.is_superuser= False
        user.is_staff = True
        user.is_active = True
        try:
            user.save()
            return JsonResponse({'Status': 'OK', 'Message' : user.username})
        except:
            return JsonResponse({'Status': 'Failed', 'Message' : 'Failed to create user'})
    return JsonResponse({'Status': 'Failed', 'Message' : 'Access Denied'})

@api_view(['POST'])
def user_update(request):
    if request.method == 'POST':
        nu = request.body;
        nu = json.loads(nu)
        username = nu['old_username']
        email = nu['old_email']
        try:
            user = AuthUser.objects.get(username=username, email=email)
            user.first_name = nu['first_name']
            user.last_name = nu['last_name']
            user.email = nu['new_email']
            user.username = nu['new_username']
            user.save()
            return JsonResponse({'Status': 'OK', 'Message' : 'User edited'})
        except:
            return JsonResponse({'Status': 'Failed', 'Message' : 'User not exist'})
    return JsonResponse({'Status': 'Failed', 'Message' : 'Access Denied'})


@api_view(['POST'])
def user_delete(request):
    if request.method == 'POST':
        nu = request.body;
        nu = json.loads(nu)
        username = nu['username']
        email = nu['email']
        try:
            user = AuthUser.objects.get(username=username, email=email)
            user.delete()
            return JsonResponse({'Status': 'OK', 'Message' : 'User deleted'})
        except:
            return JsonResponse({'Status': 'Failed', 'Message' : 'User not exist'})
    return JsonResponse({'Status': 'Failed', 'Message' : 'Access Denied'})

@api_view(['POST'])
def user_view(request):
    if request.method == 'POST':
        nu = request.body;
        nu = json.loads(nu)
        username = nu['username']
        email = nu['email']
        try:
            user = AuthUser.objects.get(username=username, email=email)
            return JsonResponse({'Status': 'OK', 'Message' : 'User given', 'User' : {'first_name': user.first_name, 'last_name': user.last_name, 'email': email, 'username': username}})
        except:
            return JsonResponse({'Status': 'Failed', 'Message' : 'User not exist'})
    return JsonResponse({'Status': 'Failed', 'Message' : 'Access Denied'})


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

def logs(request):
    response_text = textwrap.dedent('''\
        <html>
        <head>
            <title>Logs</title>
        </head>
        <body>
            <h1>Contenido del log</h1>
            <p>X</p>
        </body>
        </html>
    ''')
    return HttpResponse(response_text)


#-------------------Expediente---------------------
@api_view(['POST'])
def expediente_create(request):
    if request.method == 'POST':
        nu = request.body;
        nu = json.loads(nu)
        exp = Expediente()
        exp.solicitante = nu['solicitante']
        exp.tipo_solicitud = nu['tipo_solicitud']
        exp.asunto = nu['asunto']
        exp.documentos = nu['documentos']
        exp.fecha_creacion = nu['fecha_creacion']
        exp.fecha_modificacion = nu['fecha_modificacion']
        print exp.solicitante + "\n"
        print exp.tipo_solicitud + "\n"
        print exp.asunto + "\n"
        print exp.documentos + "\n"
        print exp.fecha_creacion + "\n"
        print exp.fecha_modificacion + "\n"
        try:
            exp.save()
            return JsonResponse({'Status': 'OK', 'Message' : 'Expediente Creado ' + str(exp.correlativo )})
        except:
            return JsonResponse({'Status': 'Failed', 'Message' : 'Failed to create Expediente'})
    return JsonResponse({'Status': 'Failed', 'Message' : 'Access Denied'})

@api_view(['POST'])
def expediente_update(request):
    if request.method == 'POST':
        nu = request.body;
        nu = json.loads(nu)
        correlativo = nu['correlativo']
        try:
            exp = Expediente.objects.get(correlativo=correlativo)
            exp.solicitante = nu['solicitante']
            exp.tipo_solicitud = nu['tipo_solicitud']
            exp.asunto = nu['asunto']
            exp.documentos = nu['documentos']
            exp.fecha_creacion = nu['fecha_creacion']
            exp.fecha_modificacion = nu['fecha_modificacion']
            exp.save()
            return JsonResponse({'Status': 'OK', 'Message' : 'Expediente updated'})
        except:
            return JsonResponse({'Status': 'Failed', 'Message' : 'Expediente not exist'})
    return JsonResponse({'Status': 'Failed', 'Message' : 'Access Denied'})

@api_view(['POST'])
def expediente_delete(request):
    if request.method == 'POST':
        nu = request.body;
        nu = json.loads(nu)
        correlativo = nu['correlativo']
        try:
            exp = Expediente.objects.get(correlativo=correlativo)
            exp.delete()
            return JsonResponse({'Status': 'OK', 'Message' : 'Expediente deleted'})
        except:
            return JsonResponse({'Status': 'Failed', 'Message' : 'Expediente not exist'})
    return JsonResponse({'Status': 'Failed', 'Message' : 'Access Denied'})

@api_view(['POST'])
def expediente_view(request):
    if request.method == 'POST':
        nu = request.body;
        nu = json.loads(nu)
        correlativo = nu['correlativo']
        try:
            exp = Expediente.objects.get(correlativo=correlativo)
            return JsonResponse({'Status': 'OK', 'Message' : 'Expediente given', 'Expediente' : {'correlativo' : correlativo, 'solicitante': exp.correlativo, 'solicitante':exp.solicitante, 'tipo_solicitud': exp.tipo_solicitud, 'asunto': exp.asunto, 'documentos': exp.documentos, 'fecha_creacion': exp.fecha_creacion, 'fecha_modificacion': exp.fecha_modificacion}})
        except:
            return JsonResponse({'Status': 'Failed', 'Message' : 'Expediente not exist'})
    return JsonResponse({'Status': 'Failed', 'Message' : 'Access Denied'})

#-------------------Acta---------------------------
@api_view(['POST'])
def acta_create(request):
    if request.method == 'POST':
        nu = request.body;
        nu = json.loads(nu)
        acta = Acta()
        acta.id_expediente = nu['id_expediente']
        acta.fecha = nu['fecha']
        acta.asunto = nu['asunto']
        acta.firma = nu['firma']

        try:
            acta.save()
            return JsonResponse({'Status': 'OK', 'Message' : 'Acta ' + str(acta.id_acta) })
        except:
            return JsonResponse({'Status': 'Failed', 'Message' : 'Failed to create Acta'})
    return JsonResponse({'Status': 'Failed', 'Message' : 'Access Denied'})

@api_view(['POST'])
def acta_update(request):
    if request.method == 'POST':
        nu = request.body;
        nu = json.loads(nu)
        id_acta = nu['id_acta']
        try:
            acta = Acta.objects.get(id_acta=id_acta)
            acta.solicitante = nu['id_expediente']
            acta.fecha = nu['fecha']
            acta.tipo_solicitud = nu['asunto']
            acta.asunto = nu['firma']
            acta.save()
            return JsonResponse({'Status': 'OK', 'Message' : 'Acta updated'})
        except:
            return JsonResponse({'Status': 'Failed', 'Message' : 'Acta not exist'})
    return JsonResponse({'Status': 'Failed', 'Message' : 'Access Denied'})

@api_view(['POST'])
def acta_delete(request):
    if request.method == 'POST':
        nu = request.body;
        nu = json.loads(nu)
        id_acta = nu['id_acta']
        try:
            acta = Acta.objects.get(id_acta=id_acta)
            acta.delete()
            return JsonResponse({'Status': 'OK', 'Message' : 'Acta deleted'})
        except:
            return JsonResponse({'Status': 'Failed', 'Message' : 'Acta not exist'})
    return JsonResponse({'Status': 'Failed', 'Message' : 'Access Denied'})

@api_view(['POST'])
def acta_view(request):
    if request.method == 'POST':
        nu = request.body;
        nu = json.loads(nu)
        id_acta = nu['id_acta']
        try:
            acta = Acta.objects.get(id_acta=id_acta)
            return JsonResponse({'Status': 'OK', 'Message' : 'Acta given', 'Acta' : {'id_acta': id_acta, 'id_expediente': acta.id_expediente, 'fecha':acta.fecha, 'asunto': acta.asunto, 'firma': acta.firma}})
        except:
            return JsonResponse({'Status': 'Failed', 'Message' : 'Acta not exist'})
    return JsonResponse({'Status': 'Failed', 'Message' : 'Access Denied'})