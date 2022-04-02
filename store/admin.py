from django.contrib import admin
from .models import *


# Register your models here.

class categdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(categ, categdmin)


class prodadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'slug', 'price', 'stock', 'img','available',]
    list_editable = ['price', 'stock', 'img']


admin.site.register(product, prodadmin)
