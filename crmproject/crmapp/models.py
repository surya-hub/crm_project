from django.db import models
from django.contrib.auth.models import AbstractUser,User

class Customer(models.Model):
    first_name=models.CharField(max_length=100,null=True,blank=True)
    last_name=models.CharField(max_length=100,null=True,blank=True)
    username = models.CharField(max_length=100, null=True, blank=True)
    email=models.EmailField(max_length=100,null=True,blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    mobile = models.BigIntegerField()
    create_date=models.DateField(auto_now=True,null=True,blank=True)
    def __str__(self):
        return self.first_name

class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    description=models.CharField(max_length=100)
    order_date=models.DateField(auto_now=True)
    CATEGORY_CHOICES=(
        ('indoor','INDOOR'),
        ('outdoor','OUTDOOR'),
        ('Anywhere','ANYWHERE')
    )
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=100)
    def __str__(self):
        return self.name

class Order(models.Model):
    customer=models.ForeignKey(Customer,null=True,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,null=True,on_delete=models.CASCADE)
    STATUS_CHOICES=(
        ('delivered','DELIVERED'),
        ('pending','PENDING'),
        ('outfor delivery','OUTFOR DELIVERY')
    )
    status=models.CharField(choices=STATUS_CHOICES,max_length=100)
    created_date=models.DateField(auto_now=True,null=True)
    def __str__(self):
        return  self.status
