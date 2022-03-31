# Generated by Django 4.0.3 on 2022-03-31 14:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='adults',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(6)]),
        ),
        migrations.AddField(
            model_name='reservation',
            name='kids',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(6)]),
        ),
    ]
