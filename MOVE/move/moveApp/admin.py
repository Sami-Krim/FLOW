from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import CustomUserCreationForm
from .models import Clients, GrandLivres, Operations, Utilisateurs, Comptes, Mouvements

class UserAdmin(BaseUserAdmin):
    add_form = CustomUserCreationForm
    list_display = ('username', 'nomUtil', 'preUtil', 'nivUtil', 'serviceUtil', 'dateCreUtil', 'heureCreUtil', 'derniereOperUtil')
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'nomUtil', 'preUtil', 'nivUtil', 'serviceUtil', 'dateCreUtil', 'heureCreUtil', 'derniereOperUtil'),
        }),
    )
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('nomUtil', 'preUtil', 'nivUtil', 'serviceUtil', 'dateCreUtil', 'heureCreUtil', 'derniereOperUtil')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login',)}),
    )

admin.site.register(Utilisateurs, UserAdmin)
admin.site.register(Clients)
admin.site.register(GrandLivres)
admin.site.register(Operations)
admin.site.register(Comptes)
admin.site.register(Mouvements)