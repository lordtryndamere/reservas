from django import forms
from .models import Usuario
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Usuarioform(forms.ModelForm):
    class Meta:
        model = Usuario
        fields  = [
            'id' ,
            'tipo_identificaicon',
            'nombres' ,
            'apellidos',
            'fecha_nacimiento' ,
            'sexo' ,
            'Email',  
            'rol' , 
        
        ]

        labels = {
             'id' : 'Identificacion',
             'tipo_identificaicon' : 'Tipo De Identificacion',
             'nombres' : 'Nombres',
             'apellidos' : 'Apellidos',
             'fecha_nacimiento' : ' Fecha De Nacimiento',
             'sexo' : 'Sexo',
             'Email':'Correo Electronico', 
             'rol' : 'Tipo de Solicitante', 
        }

        widgets  = {
             'id' : forms.TextInput(attrs={'class':'form-control'}),
             'tipo_identificaicon' : forms.Select(attrs={'class':'form-control'}),
             'nombres' :forms.TextInput(attrs={'class':'form-control'}),
             'apellidos' : forms.TextInput(attrs={'class':'form-control'}),
             'fecha_nacimiento' :forms.TextInput(attrs={'class':'form-control'}),
             'sexo' :forms.Select(attrs={'class':'form-control'}),
             'Email' : forms.TextInput(attrs={'class':'form-control'}),
             'rol' :forms.Select(attrs={'class':'form-control'}),
        }  


class UsuarioRegistrar(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
        ]

        labels = {
            'username' :'Username',
            'email':'Email',

            }