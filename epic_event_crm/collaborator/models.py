from django.contrib.auth.models import AbstractUser
from django.db import models


class Collaborator(AbstractUser):
    ROLE_CHOICES = [
        ('gestion', 'Gestion'),
        ('commercial', 'Commercial'),
        ('support', 'Support'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

