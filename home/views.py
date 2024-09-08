from django.shortcuts import render
from services.models import Product
# Create your views here.


def index(request):

    product = Product.objects.all()
    context = {
        'product_list': product,
    }

    return render(request, 'home/index.html', context)

def about(request):
    return render(request, 'home/about.html')
