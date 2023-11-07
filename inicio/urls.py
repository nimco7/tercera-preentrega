from django.urls import path
from inicio.views import inicio, productos, crear_producto, crear_categoria, crear_resenia

urlpatterns = [
    path("", inicio, name="inicio"),
    path("productos/", productos, name="productos"),
    path("productos/crear", crear_producto, name="crear_producto"),
    path("productos/categoria", crear_categoria, name="crear_categoria"),
    path("productos/reseña", crear_resenia, name="crear_resenia"),
]
