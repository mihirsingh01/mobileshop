from django.db import models
from django.contrib.auth.models import User

class SaleCollection(models.Model):
    product_name = models.CharField(max_length=100)
    mrp = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    payment_type = models.CharField(max_length=20)
    payment_status = models.CharField(max_length=20)
    sales_person = models.ForeignKey(User, on_delete=models.CASCADE)
    date_collected = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product_name} sold by {self.sales_person.username} - {self.payment_status}"
