from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from cloudinary.models import CloudinaryField


RATINGS = ((None, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'))

# Create your models here.


class Product(models.Model):
    item = models.IntegerField(null=True)
    name = models.CharField(max_length=254)
    url = models.SlugField(max_length=300, null=True, unique=True)
    image = CloudinaryField('image', default='dfy0one9z', blank=True)
    description = models.TextField(
        validators=[
            MinLengthValidator(1)
            ]
        )
    summary = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        ordering = ['-item']

    def __str__(self):
        return self.name


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=500)
    rating = models.IntegerField(choices=RATINGS, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.comment} - by {self.user}"