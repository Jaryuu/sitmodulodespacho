from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from sitmoduloregistro.quickstart.serializers import UserSerializer, GroupSerializer
import json
import textwrap
from django.http import HttpResponse
from django.http import JsonResponse

from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from models import *

class UserForm(ModelForm):
    class Meta:
        model = AuthUser
        fields = "__all__"

def user_list(request, template_name='users/user_list.html'):
    return JsonResponse({'Status': 'Failed', 'Message' : 'Access Denied'})

def user_create(request):
    if request.method == 'POST':
        nu = request.body;
        user = AuthUser()
        user.password = nu['password']
        user.first_name = nu['first_name']
        user.last_name = nu['last_name']
        user.email = nu['email']
        user.username = nu['username']
        user.is_superuser= False
        user.is_staff = nu['is_staff']
        user.is_active = True
        if(user.save()):
            return JsonResponse({'Status': 'OK', 'Message' : user.username})
        else:
            return JsonResponse({'Status': 'Failed', 'Message' : 'Failed to create user'})
    return JsonResponse({'Status': 'Failed', 'Message' : 'Access Denied'})


def user_update(request):
    """server = get_object_or_404(User, pk=pk)
    form = UserForm(request.POST or None, instance=server)
    if form.is_valid():
        form.save()
        return redirect('user_list')
    return JsonResponse({'foo':''})"""
    return JsonResponse({'Status': 'Failed', 'Message' : 'Access Denied'})

def user_delete(request):
    if request.method == 'POST':
        nu = request.body;
        username = nu['email']
        email = nu['username']
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
