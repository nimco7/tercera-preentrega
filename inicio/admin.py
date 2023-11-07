from django.contrib import admin
from inicio.models import Producto, Categoria
# Register your models here.
admin.site.register([Producto, Categoria])