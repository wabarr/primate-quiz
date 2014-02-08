from django.contrib import admin
from primatequiz.models import *

# Register your models here.

class speciesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("commonname",)}

admin.site.register(species, speciesAdmin)
admin.site.register(question)