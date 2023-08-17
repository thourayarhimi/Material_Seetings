from django.contrib import admin
from .models import FileMs
from .models import File,condition,resulta,rute,lm,EquipeMS

# Register your models here.

admin.site.register(lm)
admin.site.register(condition)
admin.site.register(resulta)
admin.site.register(rute)
admin.site.register(FileMs)
admin.site.register(File)
admin.site.register(EquipeMS)

