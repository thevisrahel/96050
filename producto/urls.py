from django.urls import path
from producto.views import inicio, datos, productos, crear_producto, listar_productos, detalle_producto, actualizar_producto, eliminar_producto

app_name ='producto'

urlpatterns = [
    path('', inicio, name ='inicio'),
    path('datos/', datos),
    # path('productos/', productos),
    path('crear_producto/', crear_producto, name = 'crear_producto'),
    path('productos/', listar_productos, name='listar_productos'),
    path('productos/<int:id_producto>/', detalle_producto, name='detalle'),
    path('productos/<int:id_producto>/actualizar/', actualizar_producto, name='actualizar'),
    path('productos/<int:id_producto>/eliminar/', eliminar_producto, name='eliminar'),
]



