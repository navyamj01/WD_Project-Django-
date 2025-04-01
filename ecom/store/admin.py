from django.contrib import admin
from .models import Category, Customer, order, Products
# Register your models here.

admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(order)
admin.site.register(Products)
