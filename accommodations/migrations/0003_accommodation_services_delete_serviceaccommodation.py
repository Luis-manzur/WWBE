# Generated by Django 4.0.3 on 2022-03-17 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accommodations', '0002_alter_accommodation_name_alter_image_accommodations'),
    ]

    operations = [
        migrations.AddField(
            model_name='accommodation',
            name='services',
            field=models.ManyToManyField(to='accommodations.service'),
        ),
        migrations.DeleteModel(
            name='ServiceAccommodation',
        ),
    ]
