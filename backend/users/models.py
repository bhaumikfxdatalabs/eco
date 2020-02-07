from django.contrib.auth.models import AbstractUser
from django.db import models
from users.managers import CustomUserManager
from django.utils import timezone


class CustomUser(AbstractUser):
    # add additional fields in here
    username = None
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True)
    age = models.IntegerField(null=True, blank=True)
    joined_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
