from django.contrib import admin

# Register your models here.
from .models import Work
from .models import AddedWork

admin.site.register(Work)
admin.site.register(AddedWork)