from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import User
from pkg_resources import require
from .managers import CustomUserManager
# Create your models here.




class CustomUser(AbstractBaseUser):
    username = None
    id = models.AutoField(primary_key=True)
    mobile = models.BigIntegerField(null=True, blank=True)
    email = models.EmailField(max_length=255, unique=True)
    is_varified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    def __str__(self):
        return self.email
    