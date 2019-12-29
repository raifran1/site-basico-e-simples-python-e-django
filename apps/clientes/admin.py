from django.contrib import admin
from .models import Cliente
# Register your models here.

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('name', 'cpfCnpj','mobilePhone')
    search_fields = ('name','cpfCnpj')
    #list_filter = ('status_disponibilidade')
    #list_editable = ('status_disponibilidade',)