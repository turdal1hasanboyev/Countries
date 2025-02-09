from django.db import models


class BaseModel(models.Model):
    """Base Model"""
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        verbose_name = 'Asosiy Model'
        verbose_name_plural = 'Asosiy Model'


class SubEmail(BaseModel):
    """SubEmail Model"""
    email = models.EmailField(max_length=50, unique=True, db_index=True)

    class Meta:
        verbose_name = 'SubEmail Model'
        verbose_name_plural = 'SubEmail Model'

    def __str__(self):
        return f"{self.email}"
