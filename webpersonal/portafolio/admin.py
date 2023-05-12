from django.contrib import admin
from .models import project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('crear', 'actualizar')


admin.site.register(project,ProjectAdmin)

