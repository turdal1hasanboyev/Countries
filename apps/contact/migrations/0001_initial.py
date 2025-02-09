# Generated by Django 5.1.6 on 2025-02-09 03:56

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('email', models.EmailField(db_index=True, max_length=50, unique=True)),
                ('phone_number', models.CharField(db_index=True, max_length=20, unique=True)),
                ('message', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Aloqa',
                'verbose_name_plural': 'Aloqa',
            },
        ),
    ]
