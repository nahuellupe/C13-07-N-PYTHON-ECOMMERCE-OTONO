from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=250)
    category = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    image_url = models.FileField(max_length=500, blank=True)

    def __str__(self):
        return self.name
