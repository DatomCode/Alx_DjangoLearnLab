from django.contrib import admin

# Register your models here.
from .models import Book

admin.ModelAdmin
admin.site.register(Book)