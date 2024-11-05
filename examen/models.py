from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.


# Se expone un escenario de una página Web, con un modelo Principal 
# que debéis incluir al menos tres atributos que tengan sentido.

#Choices el segundo valor es el que se muestra es humano, pero vaya, que es lo mismo, difiero por puntos.
MATERIAL_BOLSO = (
    ("Cuero.", "Cuero"),
    ("Tela.", "Tela"),
    ("Plastico PVC", "Plastico"),
    ("Lona.","Lona"),
    
)

BANCOS = (
    ("Caixa.", "Caixa."),
    ("BBVA", "BBVA."),
    ("UNICAJA", "UNICAJA."),
    ("ING", "ING.")
)

class Bolso(models.Model):
    id_bolso = models.AutoField(primary_key=True)
    preciobolso = models.IntegerField()
    fabricantebolso = models.TextField(max_length=50)
    longitudcorrea = models.TextField(max_length=100) #En centimetros
    materialbolso = models.TextField(max_length=12, choices=MATERIAL_BOLSO)

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key = True)
    nombreusuario = models.TextField(max_length=20)
    telefonousuario = models.CharField(max_length=9) #Se predecide que la web es española y prefijo +34, de ahi 9 digitos solo
    direccion = models.TextField(max_length=30)
    fecharegistrocuenta = models.DateTimeField(default=timezone.now)
    votante_adscrito = models.BooleanField() #Lo utilizare para filtrar quien vota o no.
    
class SistemaVotaciones(models.Model):
    id_votacion = models.AutoField(primary_key=True)
    puntuacion_proyecto = models.PositiveIntegerField() #De 1 hacia 5 tecnicamente, no se valida prompt del todo
    comentario = models.TextField(max_length=300) #Incluimos comentarios largos
    registrovotacion = models.DateTimeField(default=timezone.now)
    usuario = models.OneToOneField(Usuario, on_delete = models.CASCADE)
    modelovotado = models.TextField(max_length=10, default="Bolso")  
    
    #Relacion uno a uno, el usuario solo podra votar a un modelo principal.
    
#PositiveIntegerField esta en la documentacion oficial de Django, es un tipo de modelo que nos permite
#tener un entero del 0 al 2147483647, no aceptará negativos, ya que el sistema de votaciones es de 1 a 5
#por lo menos voy a hacer que sean positivos, aunque no se pida, el numero 0 se acepta por razones de
#compatibilida en Django, pero al menos me aseguro que salgan de 0, incluido, en adelante (max_length = 1)

#Link: https://docs.djangoproject.com/en/5.1/ref/models/fields/


class CuentaBancaria(models.Model):
    id_cuentabancaria = models.AutoField(primary_key=True)
    bancoasociado = models.TextField(max_length = 10, choices = BANCOS)
    saldocuenta = models.FloatField(max_length=20)
    titularcuenta = models.OneToOneField(Usuario, on_delete = models.CASCADE) #USUARIO
    
    