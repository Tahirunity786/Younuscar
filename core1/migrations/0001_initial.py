# Generated by Django 5.0.1 on 2024-01-11 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tokken_id', models.CharField(default='', max_length=100)),
                ('reg_number', models.CharField(default='', max_length=50)),
                ('name', models.CharField(default='', max_length=100)),
                ('year', models.CharField(default='', max_length=5)),
                ('engine', models.CharField(default='', max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(db_index=True, default='', max_length=100)),
                ('last_name', models.CharField(db_index=True, default='', max_length=100)),
                ('street_no', models.CharField(db_index=True, default='', max_length=200)),
                ('postal_code', models.CharField(db_index=True, default='', max_length=50)),
                ('city', models.CharField(db_index=True, default='', max_length=100)),
                ('state', models.CharField(db_index=True, default='', max_length=100)),
                ('country', models.CharField(db_index=True, default='', max_length=100)),
            ],
        ),
    ]