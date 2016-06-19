from django.contrib import admin
from plants.models import Plantkind, Plant


# Register your models here.

class PlantkindAdmin(admin.ModelAdmin):
	list_display = ('name','introduce')

class PlantAdmin(admin.ModelAdmin):
	list_display = ('name','plantkind')
	search_fields = ('name',)


admin.site.register(Plantkind,PlantkindAdmin)
admin.site.register(Plant,PlantAdmin)