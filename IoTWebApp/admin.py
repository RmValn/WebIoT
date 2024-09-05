from django.contrib import admin
from .models import User
# Register your models here.

@admin.register(User)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('username','email',"last_name", "first_name")