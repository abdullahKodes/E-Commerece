from django.db import models
from Categories.models import Category
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='products', blank=True, null=True)

    def __str__(self):
        return self.name

