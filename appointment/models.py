from django.db import models


class Appointment(models.Model):
    """
    The model indicates to booking and manage appointments
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    request = models.TextField(blank=True)
    sent_date = models.DateField(auto_now_add=True)
    accepted = models.BooleanField(default=False)
    appointment_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Request: {self.sent_date} - by {self.first_name}"

    class Meta:
        ordering = ["-sent_date"]
