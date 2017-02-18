from django.contrib import admin
from models import PickUpLine
# Register your models here.

class PickUpLineAdmin(admin.ModelAdmin):
    pass
admin.site.register(PickUpLine, PickUpLineAdmin)