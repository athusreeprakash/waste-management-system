from django.db import models
from django.contrib.auth.models import User


class UserType(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type


class UserRegistration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    point = models.IntegerField()
    pincode = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.name


class CollectorRegistration(models.Model):
    collector_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    point = models.IntegerField(null=True)

    def __str__(self):
        return self.name


class WastePickup(models.Model):
    userid = models.ForeignKey(UserRegistration, on_delete=models.CASCADE, null=True)
    collector = models.ForeignKey(CollectorRegistration, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=100)
    rdate = models.DateTimeField()
    pdate = models.DateField(null=True)

    def __str__(self):
        return self.status


class CollectionHistory(models.Model):
    pid = models.ForeignKey(WastePickup, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    weight = models.FloatField(null=True)
    point = models.IntegerField(null=True)


class Products(models.Model):
    name = models.CharField(max_length=100)
    rate = models.IntegerField(null=True)
    point = models.IntegerField(null=True)
    desc = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/', null=True)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Purchase(models.Model):
    user = models.ForeignKey(UserRegistration, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=1, null=True)
    mobile = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    pincode = models.CharField(max_length=20)
    type = models.CharField(max_length=2)
    date = models.DateField()
    status = models.CharField(max_length=20, null=True)
    total = models.IntegerField(null=True)


class StockHis(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    stock = models.IntegerField(null=True)


class OrderUpdates(models.Model):
    order = models.ForeignKey(Purchase, on_delete=models.CASCADE, null=True)
    update = models.CharField(max_length=100)
    date = models.DateField()
    status = models.CharField(max_length=20, null=True)


class Complaints(models.Model):
    user = models.ForeignKey(UserRegistration, on_delete=models.CASCADE, null=True)
    subject = models.CharField(max_length=100)
    complaint = models.CharField(max_length=200)
    rdate = models.DateField()
    sdate = models.DateField(null=True)
    status = models.CharField(max_length=20)


class Locations(models.Model):
    pincode = models.CharField(max_length=10)
