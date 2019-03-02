from django.db import models

# Create your models here.

class UsuarioRol (models.Model):
    id = models.IntegerField(primary_key=True)
    tipo_de_persona = models.CharField(max_length=20, null=True)

    def  __str__(self):
        return "{}".format(self.tipo_de_persona)

class Usuario(models.Model):
    id =  models.IntegerField(primary_key=True)
    CC = "Cedula"
    CE = "Cedula Extranjeria"
    TI  ="Tarjeta De Identidad"
    Tipo_identificaicon = ( (CC,'Cedula De Ciudadania'), (CE,'Cedula De Extranjeria'), (TI,'Tarjeta De Identidad')   )
    tipo_identificaicon  = models.CharField(max_length =20,choices=Tipo_identificaicon,default =TI)
    nombres= models.CharField(max_length =20)
    apellidos = models.CharField(max_length = 20)
    fecha_nacimiento = models.DateField(max_length=10)
    MASCULINO = 'Masculino'
    FEMENINO = 'Femenino'
    SEXOS  = ((MASCULINO,'Masculino'), (FEMENINO,'Femenino'))
    sexo  =  models.CharField(max_length =12, choices=SEXOS ,default=MASCULINO)
    Email = models.EmailField(null=True)
    rol = models.OneToOneField(UsuarioRol, blank=True, null = True, on_delete=models.CASCADE)
    


    def __str__(self):  
        return  "{}".format(self.sexo)

class Medico (models.Model):
    id = models.IntegerField(primary_key=True)
    nombres = models.CharField(max_length =20)
    apellidos  = models.CharField(max_length =20)
    cliente = models.ForeignKey(Usuario,null=True, blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return "{}".format(self.cliente)
class Reserva (models.Model):
    solicitud  = models.TextField()
    medico = models.ForeignKey(Medico,null=True,blank=True, on_delete=models.CASCADE)
    fecha_reserva =  models.DateField(auto_now_add=True)



class Disponibilidad_Agenda (models.Model):
    status  = models.BooleanField(default=True)                                   
    def  __str__(self ):
        return "{}".format(self.status)




