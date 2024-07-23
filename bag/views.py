from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages

from services.models import Product

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')