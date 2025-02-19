from django.db import models

import uuid


class Country(models.Model):
    """
    Model for Country
    """
    """
    Custom UUID field for Country model
    """
    # uuid = models.UUIDField(
    #     primary_key=True,  # UUID asosiy kalit bo‘ladi
    #     default=uuid.uuid4(),  # Har bir obyekt uchun avtomatik UUID4
    #     editable=False,  # UUID qo‘lda o‘zgartirilmasligi kerak
    #     unique=True,  # Takrorlanmasligi kerak
    #     db_index=True,  # Index qo‘shiladi, qidiruv tezlashadi
    #     verbose_name="Unique Identifier",  # Admin panel uchun tushunarli nom
    #     # Qo‘shimcha tushuntirish
    #     help_text="Auto-generated unique identifier for each country",
    #     db_column="uuid",  # Ma'lumotlar bazasidagi ustun nomi
    #     error_messages={
    #         "unique": "This UUID already exists!",  # Xatolik chiqsa tushunarli matn
    #     }
    # )
    name = models.CharField(max_length=100, unique=True,
                            db_index=True)  # Davlat nomi
    iso_code = models.CharField(
        max_length=3, unique=True, db_index=True)  # ISO kodi (UZB)
    capital = models.CharField(
        max_length=100, unique=True, db_index=True)  # Poytaxt shahri
    population = models.BigIntegerField(default=0)  # Aholi soni
    area = models.FloatField(default=0, help_text="Km²")  # Maydoni (km²)
    continent = models.CharField(max_length=50, choices=[
        ('Asia', ('Osiyo')),
        ('Europe', ('Yevropa')),
        ('Africa', ('Afrika')),
        ('North America', ('Shimoliy Amerika')),
        ('South America', ('Janubiy Amerika')),
        ('Oceania', ('Okeaniya')),
        ('Antarctica', ('Antarktika')),
    ])  # Qit'a
    currency = models.CharField(
        max_length=50, unique=True, db_index=True)  # Pul birligi (So‘m)
    phone_code = models.CharField(
        max_length=10, unique=True, db_index=True)  # Telefon kodi (+998)

    # 📌 Davlat rahbari
    leader_name = models.CharField(
        max_length=100, unique=True, db_index=True)  # Rahbar ismi
    leader_title = models.CharField(max_length=50, choices=[
        ('President', ('Prezident')),
        ('Prime Minister', ('Bosh vazir')),
        ('King', ('Qirol')),
    ])  # Lavozimi

    # 📌 Ramzlar
    flag = models.ImageField(
        upload_to='flags/', default='img/default-image.png', blank=True, null=True)  # Bayroq rasmi

    # Base
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Davlat"
        verbose_name_plural = "Davlatlar"

    def __str__(self):
        return f"{self.id}-{self.name}"
