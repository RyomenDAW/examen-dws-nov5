from django.shortcuts import render
from django.db.models import Q, Count, Avg  # Para filtros OR, agregaciones, y operaciones con modelos
from datetime import date
from .models import (
    Usuario, CuentaBancaria, Bolso, SistemaVotaciones
)


def mi_error_404(request, exception=None):
    # ERROR 404: NO SE ENCUENTRA LA PÁGINA SOLICITADA.
    return render(request, 'errores/404.html', None, None, 404)

def mi_error_400(request, exception=None):
    # ERROR 400: SOLICITUD INCORRECTA, GENERALMENTE DEBIDO A UN MAL FORMATO.
    return render(request, 'errores/400.html', None, None, 400)

def mi_error_403(request, exception=None):
    # ERROR 403: ACCESO PROHIBIDO, NO TIENE PERMISOS PARA VER ESTE RECURSO. (ADMIN)
    return render(request, 'errores/403.html', None, None, 403)

def mi_error_500(request, exception=None):
    # ERROR 500: ERROR INTERNO DEL SERVIDOR, OCURRE CUANDO HAY UN PROBLEMA NO ESPECIFICADO.
    return render(request, 'errores/500.html', None, None, 500)


#==================================================================================================

#ESTA ES LA PAGINA INDEX, AQUI IRA TODAN LAS URLS, EN TOTAL 10.
def inicio(request):
    return render(request, 'home/index.html')

#==================================================================================================

# El último voto que se realizó en un modelo principal en concreto, y mostrar el comentario, 
# la votación e información del usuario o cliente que lo realizó: 1.5 puntos
def ultimovoto_modeloconcreto_info(request, modeloconcreto):      #En modelo concreto ira bolso
    fechavotacion = SistemaVotaciones.objects.order_by('-registrovotacion')[:1]
    usuario = Usuario.objects.filter(fechavotacion)
    return render(request, 'usuarios/ultimovoto_modeloconcreto_info.html', {'usuario': usuario})


#==================================================================================================

#Todos los modelos principales que tengan votos con una puntuación numérica menor a 3 y 
# que realizó un usuario o cliente en concreto: 1.5 puntos

def modelosconvotosmenor3_cliente(request):
    modelo = Bolso.objects.filter()
    return render(request, 'bolso/modelosconvotosmenor3_cliente.html', {'modelo': modelo})


#==================================================================================================

# Todos los usuarios o clientes que no han votado nunca y mostrar información sobre estos usuarios 
# y clientes al completo: 1.5 puntos

def usuariosquenuncahanvotado(request):
    usuarios = Usuario.objects.filter(votante_adscrito=False).all()
    return render (request, 'usuarios/usuariosquenuncahanvotado.html', {'usuarios': usuarios})

#==================================================================================================

# Obtener las cuentas bancarias que sean de la Caixa o de Unicaja y que el propietario tenga un 
# nombre que contenga un texto en concreto, por ejemplo “Juan”: 1.5 puntos

def cuentasbancarias_caixa_unicaja_nombre(request, nombre):
    cuentabancaria = CuentaBancaria.objects.filter (Q (bancoasociado='Caixa') | Q(bancoasociado='UNICAJA') ) & Q ( titularcuenta=nombre)
    # procesadores = Procesador.objects.filter(  (Q(nucleos__gt=8) | Q(familiaprocesador='Intel')) & Q(hilos__gt=12) ).all()
    return render, 'cuentabancaria/cuentasbancarias_caixa_unicaja_nombre.html', {cuentabancaria: cuentabancaria}
#==================================================================================================

# Obtener los votos de los usuarios que hayan votado a partir del 2023 con una puntuación numérica 
# igual a 5  y que tengan asociada una cuenta bancaria. 1.5 puntos

def votos_apartirde2023_igual5_cuentabancaria(request):
    start_date = date(2023, 1, 1)
    end_date = date(2025, 1, 1)
    voto = SistemaVotaciones.objects.filter( Q( registrovotacion__range=[start_date, end_date]) & Q(puntuacion_proyecto=5))
    return render(request, 'votos/votos_apartirde2023_igual5_cuentabancaria.html', {'voto': voto})




#==================================================================================================

# Obtener todos los modelos principales que tengan una media de votaciones mayor del 2,5: 
# 1.5 punto

def media_mayor_a_2ymedio_bolsos(request):
    media = SistemaVotaciones.objects.aggregate(promedio=Avg('puntuacion_proyecto'))
    bolso = Bolso.objects.filter(media).all()
    return render(request, 'bolso/media_mayor_a_2ymedio_bolsos.html', {'bolso': bolso})

#SE UTILIZA LA PARTE DE AGGREGATE QUE SE TENIA QUE INVESTIGAR, SE UTILIZA PARA PODER HACER AGREGACIONES SIN CARGAR EN LA MEMORIA TODOS LOS VALORES Y DEVOLVER EL
#RESULTADO DE LAS OPERACIONES REALIZADAS CON ESOS VALORES, AHORRANDO RECURSO Y OPTIMIZANDO.

#La vista nos obtiene la media (avg) del campo nucleos de todos los objetos en el modelo Procesador, tener en cuenta que es negativo algunos valores.


# def promedio_nucleos(request):
#     promedio_nucleos = Procesador.objects.aggregate(promedio_nucleos=Avg('nucleos'))
#     return render(request, 'procesadores/promedio_nucleos.html', {'promedio_nucleos': promedio_nucleos})

#==================================================================================================
