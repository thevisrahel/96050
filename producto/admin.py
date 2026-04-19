from django.contrib import admin
from producto.models import Producto



class ProductoAdmin(admin. ModelAdmin):
    list_display = ['destino', 'descripcion']
    list_filter = ['destino']

admin.site.register(Producto, ProductoAdmin)