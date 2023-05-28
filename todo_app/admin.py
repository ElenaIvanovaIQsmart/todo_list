from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin): # ModelAdmin используется для костамизации интерфейса администратора
    readonly_fields = ('created',)

admin.site.register(Todo, TodoAdmin )


