from django.db import models
import datetime

class Category(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10, blank=True)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default=1)
    description = models.TextField(max_length=250, blank=True)
    image = models.ImageField(upload_to='uploads/product/', default='')

    def __str__(self):
        return self.name + ' (' + str(self.price) + ')'
    
class order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=200, blank=True)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='Pending')

    def __str__(self):
        return self.product.name + ' (' + str(self.quantity) + ')'