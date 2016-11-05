from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from sitmoduloregistro.quickstart.serializers import UserSerializer, GroupSerializer
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
    users = AuthUser.objects.all()
    data = {}
    data['object_list'] = users
    return JsonResponse({'foo':''})

def user_create(request, template_name='users/user_form.html'):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('user_list')
    return JsonResponse({'foo':''})

def user_update(request, pk, template_name='users/user_form.html'):
    server = get_object_or_404(User, pk=pk)
    form = UserForm(request.POST or None, instance=server)
    if form.is_valid():
        form.save()
        return redirect('user_list')
    return JsonResponse({'foo':''})

def user_delete(request, pk, template_name='users/user_confirm_delete.html'):
    server = get_object_or_404(User, pk=pk)    
    if request.method=='POST':
        server.delete()
        return redirect('user_list')
    return JsonResponse({'foo':''})



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
