from django.shortcuts import render
from .models import Usuario,UsuarioRol,Medico,Disponibilidad_Agenda,Reserva
from . forms import Usuarioform,UsuarioRegistrar
from django.views.generic import CreateView,TemplateView,DeleteView,DetailView,UpdateView,ListView
from django.urls import reverse_lazy

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeForm

class UsuarioCrear(CreateView):
    model = Usuario
    form_class = Usuarioform
    template_name = "crudreservas/usuariocrear.html"
    success_url = reverse_lazy('privado')


class UsuarioListar(ListView):
    queryset = Usuario.objects.order_by('id')
    template_name = 'crudreservas/usuariolistar.html'
    paginate_by= 5

class UsuarioMostrar(DetailView):
    model = Usuario
    template_name = 'crudreservas/usuarioshow.html'

class UsuarioDelete(DeleteView):
    model = Usuario
    template_name = 'crudreservas/usuariodelete.html'
    success_url = reverse_lazy('listar')

class UsuarioUpdate(UpdateView):
    model = Usuario
    form_class = Usuarioform
    template_name = 'crudreservas/usuarioeditar.html'
    success_url = reverse_lazy('listar')

"""def nuevo_usuario(request): ESTA ES LA FORMA DIFICIL 
    if request.method=='POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            return HttpResponseRedirect('/')
    else:
        formulario = UserCreationForm()
    return render(request,'usuarioregistrar.html',{'formulario':formulario})"""

class nuevo_usuario(CreateView):
    model = User
    form_class = UsuarioRegistrar
    template_name = 'index.html'
    success_url = reverse_lazy('login')



def ingresar (request):
     if request.method =='POST':
         formulario = AuthenticationForm(request.POST)
         if formulario.is_valid:
             usuario = request.POST['username']
             clave = request.POST ['password']
             acceso = authenticate(username=usuario,password=clave)
             if acceso is not None:
                if acceso.is_active:
                    login(request,acceso)
                    return HttpResponseRedirect('/privado')
                else:
                    return render(request,'crudreservas/noactivo.html')
             else:
                return render(request,'crudreservas/nousuario.html')
     else:
        formulario= AuthenticationForm()
     return render(request,'index.html',{'formulario':formulario})


@login_required(login_url='/ingresar')
def privado(request):
    usuario  = request.user
    return render(request,'crudreservas/privado.html',{'usuario':usuario})
