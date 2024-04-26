from django.contrib import admin
from home.models import Doctors

# Register your models here.

class DoctorsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

admin.site.register(Doctors, DoctorsAdmin)