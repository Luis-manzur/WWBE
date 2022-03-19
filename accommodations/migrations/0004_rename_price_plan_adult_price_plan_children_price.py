# Generated by Django 4.0.3 on 2022-03-17 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accommodations', '0003_accommodation_services_delete_serviceaccommodation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plan',
            old_name='price',
            new_name='adult_price',
        ),
        migrations.AddField(
            model_name='plan',
            name='children_price',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
