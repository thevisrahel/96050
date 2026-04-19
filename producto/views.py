from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template, Context, loader
from datetime import datetime

from producto.models import Producto
from producto.forms import FormularioProducto, FormularioBusqueda
#def inicio(request):
#    return HttpResponse('<h1>HOLA BIENVENIDO A MI PAGINA!!<h1>')


def inicio(request):
    
    #v1
    #archivo_abierto = open(r'C:\Users\labar\Desktop\django\producto\templates\inicio.html')
    #...
    #archivo_abierto.close()
    
    # with open(r'C:\Users\labar\Desktop\django\producto\templates\inicio.html') as archivo_abierto:
    #     template = Template(archivo_abierto.read())
        
    # fecha_y_hora_actual = datetime.now()
        
    # contexto=Context({'fecha_y_hora_actual' : fecha_y_hora_actual})
    
    # template_renderizado = template.render(contexto)
    
    # return HttpResponse(template_renderizado)

    # #v2
    # template = loader.get_template('inicio.html')
    # # with open(r'C:\Users\labar\Desktop\django\producto\templates\inicio.html') as archivo_abierto:
    # #     template = Template(archivo_abierto.read())
        
    # fecha_y_hora_actual = datetime.now()
    
    # template_renderizado = template.render({'fecha_y_hora_actual' : fecha_y_hora_actual})
    
    # return HttpResponse(template_renderizado)

    #v3
    fecha_y_hora_actual = datetime.now()
    return render(request, 'producto/inicio.html', {'fecha_y_hora_actual' : fecha_y_hora_actual})

def datos(request):
    
    # numeros =list(range(1,20))
    numeros = []
    
    return render(request, 'producto/datos.html', {"numeros" : numeros})

def productos(request):
    producto = Producto(nombre='jabon liquido', descripcion='uso para lavado de manos.')
    producto.save()
    return render(request, 'producto/productos.html', {"producto" : producto})

def crear_producto(request):
    
    #v1
    # print('GET: ', request.GET)
    # print('POST: ', request.POST)
    
    # if request.method == 'POST':
    #     producto = Producto(nombre=request.POST.get('nombre'), descripcion=request.POST.get('descripcion'))
    #     producto.save()
    
    #v2
    if request.method == 'POST':
        formulario = FormularioProducto(request.POST)
        if formulario.is_valid():
            producto = Producto(nombre=formulario.cleaned_data['nombre'], descripcion=formulario.cleaned_data['descripcion'])
            producto.save()
  
    formulario = FormularioProducto()
        
    return render(request, 'producto/crear_producto.html', {'formulario': formulario})

def listar_productos(request):
    
    formulario = FormularioBusqueda(request.GET)
    if formulario.is_valid():
        filtro_nombre = formulario.cleaned_data['nombre']
        productos = Producto.objects.filter(nombre__icontains=filtro_nombre)
    else:
        productos = Producto.objects.all()
    
    return render(request, 'producto/listar_productos.html', {'productos': productos, 'formulario': formulario})

def detalle_producto(request, id_producto):
    producto = Producto.objects.get(id=id_producto)
    return render(request,'producto/detalle_productos.html', {'producto': producto})

def eliminar_producto(request, id_producto):
    producto = Producto.objects.get(id=id_producto)
    producto.delete()
    return redirect('producto:listar_productos')

def actualizar_producto(request, id_producto):
    producto = Producto.objects.get(id=id_producto)

    if request.method == "POST":
        formulario = FormularioProducto(request.POST)
        if formulario.is_valid():
            info_nueva = formulario.cleaned_data
            producto.nombre = info_nueva['nombre']
            producto. descripcion = info_nueva['descripcion']
            
            producto. save()
            return redirect('producto:listar_productos')
    else:
        formulario = FormularioProducto()
        
    return render(request, 'producto/actualizar_producto.html', {'formulario': formulario, 'producto': producto})