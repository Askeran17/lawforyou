from django.shortcuts import render
from .models import LawFaq

# Create your views here.

def faqView(request):
    faqs = LawFaq.objects.all().order_by("faq_item")
    context = {
        'faq_list': faqs,
    }

    return render(request, 'faq/faq.html', context)