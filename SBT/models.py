from django.db import models

# Create your models here.

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10, unique=True)
    email = models.EmailField(max_length=100,unique=True)
    dob = models.DateField()
    doa = models.DateField()
    address = models.TextField(max_length=200)
    def __str__(self):
        return self.email

class Expenses(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=70)
    item_price = models.FloatField()
    item_qty = models.IntegerField()
    vendor_name = models.CharField(max_length=100)
    dop = models.DateField()

    def __str__(self):
        return self.id
