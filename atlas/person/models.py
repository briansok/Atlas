from django.db import models
from django.contrib.auth.models import AbstractUser

class Person(AbstractUser):
    ROLES = (
        ('admin', 'Administrator'),
        ('employ', 'Employee'),
    )
    role = models.CharField(max_length=7, choices=ROLES, default='employ')