from django.contrib import admin

# Register your models here.
from .models import Employee, Vote

admin.site.register(Employee)
admin.site.register(Vote)