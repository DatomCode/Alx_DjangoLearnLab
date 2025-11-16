from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length = 200)
    author = models.CharField(max_length = 200)
    publication_year = models.IntegerField()

    class Meta:
        # Define the custom permissions here
        permissions = [
            ("can_view", "Can view all books"),
            ("can_create", "Can create new books"),
            ("can_edit", "Can edit existing books"),
            ("can_delete", "Can delete books"),
        ]

    def __str__(self):
        return self.title


# --- Custom User Manager (Step 3) ---

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifier
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        The fields 'date_of_birth' and 'profile_photo' are optional
        for superuser creation, but added to the model.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(('Superuser must have is_superuser=True.'))
        
        # Superuser creation typically doesn't require date_of_birth or profile_photo,
        # but we ensure they are handled if provided.
        # Set default values if not provided for date_of_birth (or make it optional).
        # We'll rely on the model definition allowing null/blank for date_of_birth and ImageField.

        return self.create_user(email, password, **extra_fields)

# --- Custom User Model (Step 1) ---

class CustomUser(AbstractUser):
    """
    Custom user model extending AbstractUser to include additional fields.
    We are setting 'email' as the unique identifier and removing 'username'.
    """
    email = models.EmailField(('email address'), unique=True)
    
    # New custom fields
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)
    
    # Set the email field as the unique identifier for authentication
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # No other fields are required beyond email and password
    
    objects = CustomUserManager() # Use the custom manager
    
    def __str__(self):
        return self.email