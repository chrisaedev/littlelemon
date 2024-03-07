from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Table(models.Model):
    table_number = models.IntegerField()
    booking_date_time = models.DateTimeField()
    customer_name = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=15)

    def __str__(self):
        return f"Table {self.table_number} - {self.customer_name}"
