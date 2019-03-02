from django.conf.urls import url
from .views import UsuarioCrear,UsuarioListar,UsuarioMostrar,UsuarioDelete,UsuarioUpdate,nuevo_usuario



urlpatterns = [

    url (r'^nuevo/', UsuarioCrear.as_view(),name="usuario_crear"),
    url (r'^listar/',UsuarioListar.as_view(),name ='listar'),
    url (r'^mostrar(?P<pk>\d+)/$' ,UsuarioMostrar.as_view(),name = 'mostrar'), 
    url(r'^eliminar/(?P<pk>\d+)/$', UsuarioDelete.as_view(), name='eliminar'),
    url(r'^editar/(?P<pk>\d+)/$', UsuarioUpdate.as_view(), name='editar'),
    url(r'^registro$',nuevo_usuario.as_view(),name='registro'),


 
    ]

