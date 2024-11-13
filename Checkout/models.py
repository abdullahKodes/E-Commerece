from django.db import models
from django.contrib.auth.models import User
from Cart.models import Cart
# Create your models here.


class Checkout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, default=None)
    last_name = models.CharField(max_length=50, default=None)
    country = models.CharField(max_length=50, default=None)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=20)
    phone = models.IntegerField()
    email = models.EmailField(null=True, blank=True)
    cart = models.ManyToManyField(Cart, related_name='order')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s order Created on {self.created_on} Successfully"
