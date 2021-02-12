from django.contrib.auth.models import AbstractUser

# Create your models here.
from django.db import models


class User(AbstractUser):
    phone_number = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.username} this is USER"
