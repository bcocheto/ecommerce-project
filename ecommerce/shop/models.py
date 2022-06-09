from django.db import models

class Order(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    total_value = models.IntegerField()
    active = models.BooleanField()

class Product(models.Model):
    name = models.CharField(max_length=200)
    inventory = models.IntegerField()
    unity_price = models.FloatField()
    image = models.TextField()
    active = models.BooleanField()

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    discount = models.DecimalField(decimal_places=2, max_digits=9)
