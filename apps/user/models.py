from django.contrib.auth.models import AbstractUser
from django.db import models
from apps.user.managers.user_manager import UserManager

class UserRole(models.TextChoices):
    ADMIN = "ADMIN", "Admin"
    USER = "USER", "User"

class User(AbstractUser):

    username = None

    name = models.CharField(max_length=100)

    email = models.EmailField(
        unique=True,
        db_index=True
    )

    role = models.CharField(
        max_length=20,
        choices=UserRole.choices,
        default=UserRole.USER
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        db_table = "users"
    
    def __str__(self):
        return self.email