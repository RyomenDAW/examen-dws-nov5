from django.urls import path, re_path
from . import views


urlpatterns = [
    
]




# r'^graficas/(?P<nombre_familia>[-\w]+)/(?P<cantidad_vram>[-\w\.]+)/$': Esta es la expresión regular que define la estructura de la URL.

# ^graficas/: El símbolo ^ indica que la URL debe comenzar con "graficas/".
# (?P<nombre_familia>[-\w]+): Aquí se captura un parámetro llamado nombre_familia. La sintaxis (?P<nombre_familia>...) significa que queremos capturar esta parte de la URL en un grupo nombrado llamado nombre_familia.
# [-\w]+ significa que nombre_familia puede contener caracteres alfanuméricos (\w), guiones (-), y debe tener una longitud de al menos un carácter (+).
# /(?P<cantidad_vram>[-\w\.]+)/: Este segundo grupo captura un parámetro llamado cantidad_vram, que sigue la misma lógica: puede contener caracteres alfanuméricos, guiones, y puntos (\.) y debe tener al menos un carácter.
# $: El símbolo $ indica el final de la URL.
# En resumen, esta expresión regular coincidiría con URLs como:

# /graficas/serie-gtx/8.0/
# /graficas/rtx-3000/10-0/
# views.lista_graficas_segunfamilia_y_vram: Es la vista que se llama cuando la URL coincide con la expresión regular.

# name='lista_graficas_segunfamilia_y_vram': Asigna un nombre a esta ruta para referenciarla desde otras partes del código.

# Ejemplo de URL y Parámetros Extraídos
# Si la URL es /graficas/rtx-3090/24.0/, entonces:

# nombre_familia sería 'rtx-3090'
# cantidad_vram sería '24.0'
# Estos parámetros se pasan automáticamente a la vista lista_graficas_segunfamilia_y_vram como argumentos.

# Otro Ejemplo Explicado
# Supongamos que queremos capturar una URL para los detalles de un libro en una librería online:

# python
# Copy code
# re_path(r'^libro/(?P<categoria>[-\w]+)/(?P<id_libro>\d+)/$', views.detalle_libro, name='detalle_libro')
# Esta línea hace lo siguiente:

# ^libro/: La URL debe comenzar con "libro/".
# (?P<categoria>[-\w]+): Captura un parámetro llamado categoria que puede tener letras, números, y guiones.
# /(?P<id_libro>\d+)/: Captura un parámetro llamado id_libro, que debe ser un número (\d+).
# $: Indica el final de la URL.
# Con esto, la URL /libro/ficcion/123/ llamaría a la vista detalle_libro, pasando los valores:

# categoria: 'ficcion'
# id_libro: 123
# Este patrón permite que re_path defina rutas de URL complejas que capturen parámetros variados para pasarlos a las vistas, lo cual es útil para generar URLs dinámicas en Django.