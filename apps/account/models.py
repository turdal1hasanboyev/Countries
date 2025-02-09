from django.db import models

from django.contrib.auth.models import AbstractUser

from ckeditor.fields import RichTextField

from apps.base.models import BaseModel
from .manager import CustomUserManager


class CustomUser(BaseModel, AbstractUser):
    """
    Custom User Model

    fields:
    username = None
    firs_name = null=True, blank=True
    last_name = null=True, blank=True
    """
    username = None # Username none
    first_name = models.CharField(max_length=150, blank=True, null=True) # null=True
    last_name = models.CharField(max_length=150, blank=True, null=True) # null=True
    email = models.EmailField(max_length=150, unique=True, db_index=True)
    description = RichTextField(null=True, blank=True)
    image = models.ImageField(
        upload_to='users', default='img/default-user.png', null=True, blank=True)
    
    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [] # Shu holatda turishi kerak

    class Meta:
        verbose_name = "Foydalanuvchi"
        verbose_name_plural = "Foydalanuvchilar"

    def __str__(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.email
