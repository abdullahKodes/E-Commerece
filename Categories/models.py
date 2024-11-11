from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products', blank=True, null=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name