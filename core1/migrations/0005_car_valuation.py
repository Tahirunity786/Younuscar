# Generated by Django 5.0.1 on 2024-01-11 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core1', '0004_remove_car_valuation_car_level_1_car_level_2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='valuation',
            field=models.IntegerField(default=0),
        ),
    ]
