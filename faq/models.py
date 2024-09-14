from django.db import models

# Create your models here.

class LawFaq(models.Model):
    
    title = models.CharField(max_length=300)
    question = models.CharField(max_length=300)
    answer = models.TextField(max_length=1500)

    class Meta:
        verbose_name_plural = 'FAQS'

    def __str__(self):
        return self.title



    

        
    




