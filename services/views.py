from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Product

# Create your views here.

class ServiceTemplateView(generic.ListView):
    template_name = 'services/services.html'
    queryset = Product.objects.all()
    paginate_by = 6

def product_detail(request, slug):
    """ A view to show individual product details """
    queryset = Product.objects.all()
    product = get_object_or_404(queryset, url=slug)

    context = {
        'product': product,
    }

    return render(request, 'services/product_detail.html', context)