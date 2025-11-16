from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

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



# --- Custom Admin Model (Step 4) ---

class CustomUserAdmin(UserAdmin):
    """
    Define the admin interface for the CustomUser model.
    """
    # Define the fields to be displayed in the list view
    list_display = (
        'email', 
        'first_name', 
        'last_name', 
        'is_staff',
        'date_of_birth', # Include the new field
    )
    
    # Fields to display in the user editing form
    fieldsets = (
        (None, {'fields': ('email', 'password')}), # Use email for authentication
        (('Personal info'), {'fields': (
            'first_name', 
            'last_name', 
            'date_of_birth',  # Include the new field
            'profile_photo',  # Include the new field
        )}),
        (('Permissions'), {'fields': (
            'is_active', 
            'is_staff', 
            'is_superuser',
            'groups', 
            'user_permissions',
        )}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    
    # Define fields for searching users
    search_fields = ('email',)
    # Use the custom manager for creating users
    # We remove the add_fieldsets from the default UserAdmin 
    # to simplify and rely on the CustomUserManager. 
    # For a full implementation, you would define an 'add_fieldsets' tailored for CustomUser.
    
    ordering = ('email',)


# Register the custom user model with the custom admin class
admin.site.register(CustomUser, CustomUserAdmin)