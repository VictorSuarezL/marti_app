from django.contrib import admin

from .models import Car, Brand

admin.site.register(Brand)
admin.site.register(Car)