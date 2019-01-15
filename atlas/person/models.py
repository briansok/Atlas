from django.db import models
from django.contrib.auth.models import AbstractUser


class Person(AbstractUser):
    ROLES = (
        ('admin', 'Administrator'),
        ('user', 'User'),
    )
    role = models.CharField(max_length=7, choices=ROLES, default='user')
    category = models.ForeignKey('person.Category', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        if self.first_name and self.last_name:
            return self.first_name + ' ' + self.last_name
        else:
            return self.username

    def get_edit_form(self):
        from person.forms import EditPersonForm
        return EditPersonForm(initial={
            'username': self.username,
            'email': self.email,
            'role': self.role,
            'category': self.category,
        })


class Category(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
