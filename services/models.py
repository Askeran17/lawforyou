from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Product(models.Model):
    item = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    url = models.SlugField(max_length=300, unique=True)
    image = CloudinaryField('image', default='dfy0one9z', blank=True)
    description = models.TextField()
    options = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name