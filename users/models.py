from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ObjectDoesNotExist

class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, username, password, **extra_fields)

    def authenticate(self, username_or_email, password):
        """Authenticate by username or email"""
        try:
            user = self.get(email=username_or_email)
        except ObjectDoesNotExist:
            try:
                user = self.get(username=username_or_email)
            except ObjectDoesNotExist:
                return None

        if user.check_password(password):
            return user
        return None


class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(unique=True, max_length=24)
    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username']
    objects = UserManager()

    def __str__(self):
        return self.username