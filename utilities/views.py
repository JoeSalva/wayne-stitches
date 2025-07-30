from django.shortcuts import render, redirect
from django.db.models import Q
from catalogue.models import Product, Category

# Create your views here.

def searchbox(request):
    query = request.GET.get('q')
    if query:
        product = Product.objects.filter(name__icontains=query)
    else:
        product = Product.objects.none()
    return render(request, 'search.html', {'product': product, 'query': query})

def price_filter(request):
    low = request.GET.get('low')
    high = request.GET.get('high')
    price = Product.objects.filter(price__range= (low, high))
    return render(request, 'search.html', {'price': price})