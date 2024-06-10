from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Item(models.Model):
    CATEGORY_CHOICES = [
        ('Imóvel', 'Imóvel'),
        ('Veículo', 'Veículo'),
    ]

    created_at = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='items')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    auction_date = models.DateField()
    auction_time = models.TimeField()
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)

class RealEstate(models.Model):
    item = models.ForeignKey(Item, related_name='real_estates', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    starting_price = models.DecimalField(max_digits=10, decimal_places=2)
    increment_value = models.DecimalField(max_digits=10, decimal_places=2)
    bid_history = models.JSONField(default=list)

    def __str__(self):
        return self.name

class Vehicle(models.Model):
    item = models.ForeignKey(Item, related_name='vehicles', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    starting_price = models.DecimalField(max_digits=10, decimal_places=2)
    increment_value = models.DecimalField(max_digits=10, decimal_places=2)
    bid_history = models.JSONField(default=list)

    def __str__(self):
        return self.name
