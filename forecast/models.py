from django.db import models
from django.core.validators import MinLengthValidator


# Create your models here.

class RequestHelp(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    subject = models.CharField(max_length=150)
    message = models.TextField(
        validators=[
            MinLengthValidator(1)
            ]
        )

    class Meta:
        verbose_name_plural = 'Requests'

    def __str__(self):
        return f"Request: {self.subject} - by {self.name}"