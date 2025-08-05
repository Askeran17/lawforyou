from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator


RATINGS = ((None, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'))

# Create your models here.


class Product(models.Model):
    """
    The model indicates the products
    """
    item = models.IntegerField(null=True)
    name = models.CharField(max_length=254)
    url = models.SlugField(max_length=300, null=True, unique=True)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField(
        validators=[
            MinLengthValidator(1)
            ]
        )
    summary = models.TextField(blank=True)
    cooperation_partner = models.CharField(default='Svedea', max_length=100)
    has_cooperation_partner = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        ordering = ['item']

    def __str__(self):
        return self.name


class Review(models.Model):
    """
    The model indicates the reviews for products
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=500)
    rating = models.IntegerField(choices=RATINGS, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.comment} - by {self.user}"