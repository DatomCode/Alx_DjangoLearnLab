from django.contrib import admin

# Register your models here.
from .models import Book

admin.ModelAdmin
admin.site.register(Book)

# @admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Fields to display in the admin list
    list_display = ('title', 'author', 'publication_year')

    # Fields to filter by on the right sidebar
    list_filter = ('author', 'publication_year')

    # Fields to search by (search bar at the top)
    search_fields = ('title', 'author')