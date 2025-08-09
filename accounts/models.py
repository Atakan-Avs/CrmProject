from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin - Full permissions'),
        ('manager', 'Manager - Product and category management'),
        ('user', 'User - View only'),
    ]
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='user',
        verbose_name='User Role',
        help_text='Determines the user permissions in the system'
    )

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
