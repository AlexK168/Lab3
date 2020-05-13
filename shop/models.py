from django.db import models
from django.core.validators import MaxValueValidator, EmailValidator, MinValueValidator, MinLengthValidator


# Create your models here.
class Outlet(models.Model):
    address = models.CharField(max_length=200)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.address


class Vendor(models.Model):
    email = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=400)
    country = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Product(models.Model):
    set_number = models.CharField(max_length=10, validators=[MinLengthValidator(10)])
    price = models.PositiveIntegerField(validators=[MinValueValidator])
    name = models.CharField(max_length=100)
    manufacture_date = models.DateField()
    expiry_date = models.DateField(blank=True, null=True)
    outlet = models.ForeignKey(Outlet, null=True, on_delete=models.SET_NULL)
    vendor = models.ForeignKey(Vendor, null=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Manager(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, null=True, validators=[EmailValidator()])
    phone = models.CharField(max_length=15)
    outlet = models.ForeignKey(Outlet, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name



