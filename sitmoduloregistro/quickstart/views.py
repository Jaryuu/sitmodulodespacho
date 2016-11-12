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
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
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
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
def user_update(request):
    """server = get_object_or_404(User, pk=pk)
    form = UserForm(request.POST or None, instance=server)
    if form.is_valid():
        form.save()
        return redirect('user_list')
    return JsonResponse({'foo':''})"""
    return JsonResponse({'Status': 'Failed', 'Message' : 'Access Denied'})

@api_view(['POST'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
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
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
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
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
def expediente_update(request):
    return JsonResponse({'Status': 'Failed', 'Message' : 'Access Denied'})

@api_view(['POST'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
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

#-------------------Acta---------------------------
@api_view(['POST'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
def acta_create(request):
    if request.method == 'POST':
        nu = request.body;
        nu = json.loads(nu)
        acta = Acta()
        acta.id_expediente = nu['id_expediente']
        acta.asunto = nu['asunto']
        acta.firma = nu['firma']

        try:
            acta.save()
            return JsonResponse({'Status': 'OK', 'Message' : 'Acta ' + str(acta.id_acta) })
        except:
            return JsonResponse({'Status': 'Failed', 'Message' : 'Failed to create Acta'})
    return JsonResponse({'Status': 'Failed', 'Message' : 'Access Denied'})

@api_view(['POST'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
def acta_update(request):
    return JsonResponse({'Status': 'Failed', 'Message' : 'Access Denied'})

@api_view(['POST'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
def acta_delete(request):
    return JsonResponse({'Status': 'Failed', 'Message' : 'Access Denied'})
