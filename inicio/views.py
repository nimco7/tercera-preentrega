from django.shortcuts import render, redirect
from inicio.models import Producto, Categoria, Resenia
from inicio.forms import CrearProductoFormulario, BusquedaProductoFormulario, CrearCategoriaFormulario, CrearReseniaFormulario
# Create your views here.
def inicio(request):
    return render(request, "inicio/inicio.html", {})


def productos(request):
    
    formulario = BusquedaProductoFormulario(request.GET)
    if formulario.is_valid():
        nombre_buscar = formulario.cleaned_data.get("nombre")
        listado_productos = Producto.objects.filter(nombre__icontains=nombre_buscar)
    
    formulario = BusquedaProductoFormulario()
    return render(request, "inicio/productos.html", {"formulario": formulario , "listado_productos": listado_productos})





def crear_producto(request):
    
    if request.method == "POST":
        formulario = CrearProductoFormulario(request.POST)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data

            nombre = info_limpia.get("nombre")
            descripcion = info_limpia.get("descripcion")
            anio = info_limpia.get("anio")
    
            producto = Producto(nombre=nombre, descripcion=descripcion, anio=anio)
            producto.save()
            
            return redirect("productos")
        else:
            return render(request, "inicio/crear_producto.html", {"formulario": formulario})
    
    formulario = CrearProductoFormulario()
    return render(request, "inicio/crear_producto.html", {"formulario": formulario})


def crear_categoria(request):
    if request.method == "POST":
        formulario = CrearCategoriaFormulario(request.POST)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
            
            categoria = info_limpia.get("categoria")
            categoria = Categoria(categoria=categoria)
            categoria.save()
            return redirect("inicio")
        
        return render(request, "inicio/crear_categoria.html", {"formulario": formulario})
    formulario = CrearCategoriaFormulario()
    return render(request, "inicio/crear_categoria.html", {"formulario": formulario})


def crear_resenia(request):
    if request.method == "POST":
        formulario = CrearReseniaFormulario(request.POST)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
            
            resenia = info_limpia.get("resenia")
            resenia = Resenia(resenia=resenia)
            resenia.save()
            return redirect("inicio")
        
        return render(request, "inicio/crear_resenia.html", {"formulario": formulario})
    formulario = CrearReseniaFormulario()
    return render(request, "inicio/crear_resenia.html", {"formulario": formulario})