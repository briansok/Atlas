from django.db import models
from django.contrib.auth.models import AbstractUser


class Person(AbstractUser):
    ROLES = (
        ('admin', 'Administrator'),
        ('user', 'User'),
    )
    role = models.CharField(max_length=7, choices=ROLES, default='user')
    category = models.ForeignKey('person.Category', on_delete=models.CASCADE, null=True, blank=True)


class Category(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
