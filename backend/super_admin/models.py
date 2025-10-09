from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    stock = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class OldPhone(models.Model):
    name = models.CharField(max_length=100)
    stock = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Repairing(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    description = models.TextField()
    status = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Repairing {self.product.name} - {self.status}"

class Staff(models.Model):
    name = models.CharField(max_length=100)
    attendance = models.PositiveIntegerField(default=0)
    payroll = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class CashCollection(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_collected = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cash Collection on {self.date_collected}"

class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    date_sold = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Sale of {self.product.name} - {self.quantity}"

class Purchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    date_purchased = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Purchase of {self.product.name} - {self.quantity}"
