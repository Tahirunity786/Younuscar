from django.db import models

# Create your models here.

class Packages(models.Model):
    package_name = models.CharField(max_length=100, default="", db_index=True)
    price = models.IntegerField(default=0, db_index=True)
    package_description = models.TextField(default="", db_index=True)
    product_image = models.ImageField(upload_to="product", default="", db_index=True)

class Levels(models.Model):
    level_one = models.ManyToManyField(Packages, related_name="level_one" )
    level_two = models.ManyToManyField(Packages, related_name="level_two")
    level_three = models.ManyToManyField(Packages, related_name="level_three")


class Payments(models.Model):
    # Info
    first_name = models.CharField(max_length=100, default='', db_index=True)
    last_name = models.CharField(max_length=100, default='', db_index=True)
    # contact
    postal_code = models.CharField(max_length=30, default='', db_index=True)
    # Address
    street_no = models.CharField(max_length=200, default='', db_index=True)
    postal_code = models.CharField(max_length=50, default='', db_index=True)
    city = models.CharField(max_length=100, default='', db_index=True)
    state = models.CharField(max_length=100, default='', db_index=True)
    country = models.CharField(max_length=100, default='', db_index=True)