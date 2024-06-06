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
    auction_date = models.DateTimeField(default=timezone.now)
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class RealEstate(models.Model):
    item = models.ForeignKey(Item, related_name='real_estates', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Vehicle(models.Model):
    item = models.ForeignKey(Item, related_name='vehicles', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
