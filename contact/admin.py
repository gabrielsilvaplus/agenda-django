from django.contrib import admin
from contact import models


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone_name')
    ordering = ('-id',)  # O parâmetro ordering deve ser uma tupla
    # list_filter = ('created_date',)  # Se desejar habilitar o filtro, descomente esta linha
    search_fields = ('id', 'first_name', 'last_name', 'phone_name')
    list_per_page = 10
    list_max_show_all = 200
    list_editable = ('first_name', 'last_name')  # Deve ser uma tupla
    list_display_links = ('id', 'phone_name')  # Deve ser uma tupla

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('-id',)  # O parâmetro ordering deve ser uma tupla
