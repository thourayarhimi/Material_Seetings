from django.contrib import admin
from .models import FileMs
from .models import File,condition,resulta,rute,lm,EquipeMS
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'role')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(lm)
admin.site.register(condition)
admin.site.register(resulta)
admin.site.register(rute)
admin.site.register(FileMs)
admin.site.register(File)
admin.site.register(EquipeMS)

