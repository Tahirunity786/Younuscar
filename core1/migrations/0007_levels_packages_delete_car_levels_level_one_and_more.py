# Generated by Django 5.0.1 on 2024-01-26 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core1', '0006_remove_car_level_1_remove_car_level_2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Levels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Packages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_name', models.CharField(db_index=True, default='', max_length=100)),
                ('price', models.IntegerField(db_index=True, default=0)),
                ('package_description', models.TextField(db_index=True, default='')),
                ('product_image', models.ImageField(db_index=True, default='', upload_to='product')),
            ],
        ),
        migrations.DeleteModel(
            name='Car',
        ),
        migrations.AddField(
            model_name='levels',
            name='level_one',
            field=models.ManyToManyField(related_name='level_one', to='core1.packages'),
        ),
        migrations.AddField(
            model_name='levels',
            name='level_three',
            field=models.ManyToManyField(related_name='level_three', to='core1.packages'),
        ),
        migrations.AddField(
            model_name='levels',
            name='level_two',
            field=models.ManyToManyField(related_name='level_two', to='core1.packages'),
        ),
    ]
