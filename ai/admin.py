from django.contrib import admin
from .models import *


@admin.register(Profile)
class Profile(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('user', )}
