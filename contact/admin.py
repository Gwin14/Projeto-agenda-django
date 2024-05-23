from django.contrib import admin
from contact import models

# Register your models here.


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'phone',
    ordering = 'id',
    search_fields = 'first_name', 'last_name', 'phone',

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'id', 'name',
    ordering = 'id',
    search_fields = 'name',
