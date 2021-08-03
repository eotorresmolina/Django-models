from django.contrib import admin
from applications.e_commerce.models import *

# NOTE: Tenemos que importar los modelos con los que vamos a trabajar:
# from e_commerce.models import *

# Register your models here.

# NOTE: Aquí personalizamos los campos en el Django Admin.

@admin.register(Comic)
class ComicsAdmin(admin.ModelAdmin):
    list_display = ('marvel_id', 'title', 'stock_qty', 'price')

    list_filter = ('marvel_id', 'title', 'price')

    search_fields = ('title', 'description', 'price')

    #fields = ('marvel_id', 'title', 'stock_qty')

    fieldsets = (
        (None, 
            {
                'fields': ('marvel_id', 'title', 'stock_qty')
            }
        ),
        ('Advanced Options',
            {
                'classes': ('collapse',), 
                'fields': ('description', 'price', 'picture')
            }
        )
    )

# @admin.register(Comic)
# class ComicsAdmin(admin.ModelAdmin):
    # NOTE: Para seleccionar los campos en la tabla de registros
    # list_display = ('marvel_id', 'title', 'stock_qty', 'price')

    # NOTE: Filtro lateral de elementos:
    # list_filter= ('marvel_id','title')
    
    # NOTE: Buscador de elementos en la columna:
    # search_fields = ['title']

    # NOTE: Para seleccionar los campos en el registro. 
    # fields = ('marvel_id', 'title', 'stock_qty')

    # NOTE: Genera un campo desplegable con los registros seleccionados.
    # fieldsets = (
    #     (None, {
    #         'fields': ('marvel_id', 'title', 'stock_qty')
    #     }),
    #     ('Advanced options', {
    #         'classes': ('collapse',),
    #         'fields': ('description','price', 'picture'),
    #     }),
    # )
    # pass


@admin.register(WishList)
class WishListAdmin(admin.ModelAdmin):
    list_display = ('user', 'comic', 'favorite', 'cart')

    list_filter = ('user', 'comic')

    search_fields = ('comic',)

    fieldsets = (
        (None, 
            {
                'fields': ('user', 'comic', 'favorite', 'cart')
            }
        ), 
        ('Advanced Options', 
            {
                'classes': ('collapse',), 
                'fields': ('wished_qty', 'buied_qty')
            }
        )
    )