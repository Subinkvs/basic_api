from django.db import models

# Create your models here.
class Drinks(models.Model):
    name = models.CharField(max_length=50)
    descriptions = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f'{self.name} has price {self.price}'