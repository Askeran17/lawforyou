from django.db import models

# Create your models here.


class LawFaq(models.Model):
    faq_item = models.IntegerField(null=True)
    title = models.CharField(max_length=300)
    question = models.CharField(max_length=300)
    answer = models.TextField(max_length=1500)

    class Meta:
        verbose_name_plural = 'FAQS'
        ordering = ['faq_item']

    def __str__(self):
        return self.title
