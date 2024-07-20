from django.shortcuts import render
from django.views import generic
from .models import Product

# Create your views here.

class ServiceTemplateView(generic.ListView):
    template_name = 'services/services.html'
    queryset = Product.objects.all()
    paginate_by = 6

def product_detail(request, product_id, slug):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id, slug=slug)

    context = {
        'product': product,
    }

    return render(request, 'services/product_detail.html', context)