from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.views import generic
from .models import Product
from django.contrib.auth.decorators import login_required
from .forms import ProductForm

# Create your views here.

class ServiceTemplateView(generic.ListView):
    template_name = 'services/services.html'
    queryset = Product.objects.all()
    paginate_by = 7

def product_detail(request, slug):
    """ A view to show individual product details """
    queryset = Product.objects.all()
    product = get_object_or_404(queryset, url=slug)

    context = {
        'product': product,
    }

    return render(request, 'services/product_detail.html', context)

@login_required
def edit_product(request, id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'services/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, slug):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, url=slug)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('services'))