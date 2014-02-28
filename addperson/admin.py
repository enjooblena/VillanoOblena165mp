from django.contrib import admin

# Register your models here.
from .models import newPerson

class newPersonAdmin(admin.ModelAdmin):
	class Meta:
		model = newPerson

admin.site.register(newPerson, newPersonAdmin)