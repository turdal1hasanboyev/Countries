from django.db import models

from ckeditor.fields import RichTextField

from apps.base.models import BaseModel


class Contact(BaseModel):
    """
    Contact model
    """
    name = models.CharField(max_length=100, db_index=True)
    email = models.EmailField(max_length=50, db_index=True, unique=True)
    phone_number = models.CharField(max_length=20, db_index=True, unique=True)
    message = RichTextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Aloqa'
        verbose_name_plural = 'Aloqa'

    def __str__(self):
        return f"{self.id}-{self.name}-{self.phone_number}"
