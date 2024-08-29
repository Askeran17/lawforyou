from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

RATINGS = ((None, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'))

# Create your models here.

class Product(models.Model):
    item = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    url = models.SlugField(max_length=300, unique=True)
    image = CloudinaryField('image', default='dfy0one9z', blank=True)
    description = models.TextField()
    summary = models.TextField(blank=True)
    options = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        ordering= ['-item']

    def __str__(self):
        return self.name

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=500, blank=True)
    rating = models.IntegerField(choices=RATINGS, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username