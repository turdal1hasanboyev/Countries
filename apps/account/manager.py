from django.contrib.auth.models import UserManager

import re


class CustomUserManager(UserManager):
    """
    Custom user manager class that inherits from Django's built-in UserManager.
    """

    def create_user(self, email, first_name=None, last_name=None, description=None, image=None, password=None, **extra_fields):
        if not email:
            raise ValueError(
                "Foydalanuvchilar elektron pochta manziliga ega bo'lishi kerak")
        if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
            raise ValueError(
                "Foydalanuvchilar to'g'ri elektron pochta manziliga ega bo'lishi kerak")

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name,
                          description=description, image=image, **extra_fields)
        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name=None, last_name=None, description=None, image=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser is_staff=True bo'lishi kerak")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser is_superuser=True bo'lishi kerak")

        if not email:
            raise ValueError(
                "Super Foydalanuvchilar elektron pochta manziliga ega bo'lishi kerak")
        if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
            raise ValueError(
                "Super Foydalanuvchilar to'g'ri elektron pochta manziliga ega bo'lishi kerak")

        user = self.create_user(email=email, first_name=first_name, last_name=last_name,
                                description=description, image=image, password=password, **extra_fields)
        user.is_active = True
        user.save(using=self._db)
        return user
