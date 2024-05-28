from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    starting_price = models.DecimalField(max_digits=10, decimal_places=2, default='9.99')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
