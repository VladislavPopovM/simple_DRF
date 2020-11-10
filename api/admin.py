from django.contrib import admin
from .models import Investor, Passport, Qualification

# Register your models here.
admin.site.register(Investor)
admin.site.register(Passport)
admin.site.register(Qualification)