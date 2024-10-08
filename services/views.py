from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.views import generic
from .models import Product, Review
from django.contrib.auth.decorators import login_required
from .forms import ProductForm, ReviewForm

# Create your views here.


class ServiceTemplateView(generic.ListView):
    template_name = 'services/services.html'
    queryset = Product.objects.all()
    paginate_by = 6


def product_detail(request, url):
    """ Display detailed product """
    queryset = Product.objects.all()
    product = get_object_or_404(queryset, url=url)
    reviews = product.reviews.all().order_by("-created_at")
    if request.method == "POST":
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.product = product
            review.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Review submitted')
        else:
            messages.error(request,
                           ('Failed to add review. '
                            'Ensure the form is valid and '
                            'you added a rating'))

    review_form = ReviewForm()

    return render(
        request,
        "services/product_detail.html",
        {"product": product,
            "reviews": reviews,
            "review_form": review_form, },
    )


def review_edit(request, url, review_id):
    """
    view to edit reviews
    """
    if request.method == "POST":

        queryset = Product.objects.all()
        product = get_object_or_404(queryset, url=url)
        review = get_object_or_404(Review, pk=review_id)
        review_form = ReviewForm(data=request.POST, instance=review)

        if review_form.is_valid() and review.user == request.user:
            review = review_form.save(commit=False)
            review.product = product
            review.save()
            messages.add_message(request, messages.SUCCESS, 'Review Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Failed to update, make sure you put also rating!')  # noqa

    return redirect(reverse('product_detail', args=[url]))


def review_delete(request, url, review_id):
    """
    view to delete review
    """
    queryset = Product.objects.all()
    product = get_object_or_404(queryset, url=url)
    review = get_object_or_404(Review, pk=review_id)

    if review.user == request.user:
        review.delete()
        messages.add_message(request, messages.SUCCESS, 'Review deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'Error delete!')

    return redirect(reverse('product_detail', args=[url]))


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.url]))
        else:
            messages.error(request,
                           ('Failed to add product. '
                            'Please ensure the form is valid.'))
    else:
        form = ProductForm()

    template = 'services/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, url):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, url=url)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.url]))
        else:
            messages.error(request,
                           ('Failed to update product. '
                            'Please ensure the form is valid.'))
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
def delete_product(request, url):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, url=url)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('services'))