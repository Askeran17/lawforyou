from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import generic
from django.http import HttpResponse
from services.models import Product
# Create your views here.

class HomeTemplateView(generic.ListView):
    template_name = 'home/index.html'
    queryset = Product.objects.all()
    
def featured(request, slug):
    queryset = Product.objects.all()
    product = get_object_or_404(queryset, url=slug)
    return render(request, 'home/index.html', {'product_list': product})

def about(request):
    return render(request, 'home/about.html')
