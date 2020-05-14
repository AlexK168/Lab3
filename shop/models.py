from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User


# Create your models here.
class Outlet(models.Model):
    name = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.address


class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Product(models.Model):
    set_number = models.CharField(max_length=10, validators=[MinLengthValidator(10)])
    price = models.PositiveIntegerField()
    name = models.CharField(max_length=100)
    manufacture_date = models.DateField()
    expiry_date = models.DateField(blank=True, null=True)
    outlet = models.ForeignKey(Outlet, null=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.product.name
