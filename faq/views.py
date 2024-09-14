from django.shortcuts import render
from .models import LawFaq

# Create your views here.

def faqView(request):
    faqs = LawFaq.objects.all()
    context = {
        'faq_list': faqs,
    }

    return render(request, 'faq/faq.html', context)