from django.contrib import admin
from .models import Worker, Shift
# Register your models here.

class WorkerAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','is_available']

admin.site.register(Worker, WorkerAdmin)
admin.site.register(Shift)