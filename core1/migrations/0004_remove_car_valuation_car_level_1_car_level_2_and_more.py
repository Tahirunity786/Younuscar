# Generated by Django 5.0.1 on 2024-01-11 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core1', '0003_remove_car_level_car_valuation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='valuation',
        ),
        migrations.AddField(
            model_name='car',
            name='level_1',
            field=models.BooleanField(choices=[(1, 'Level 1'), (2, 'Level 2'), (3, 'Level 3')], default=False),
        ),
        migrations.AddField(
            model_name='car',
            name='level_2',
            field=models.BooleanField(choices=[(1, 'Level 1'), (2, 'Level 2'), (3, 'Level 3')], default=False),
        ),
        migrations.AddField(
            model_name='car',
            name='level_3',
            field=models.BooleanField(choices=[(1, 'Level 1'), (2, 'Level 2'), (3, 'Level 3')], default=False),
        ),
    ]