from django.contrib import admin

# Register your models here.
from .models import project,ourwork

admin.site.register(project)
admin.site.register(ourwork)
