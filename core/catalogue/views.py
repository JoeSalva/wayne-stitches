from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Product, Category
from order.models import OrderItem,Order

# Create your views here.

def store_front(request):
    categories = Category.objects.prefetch_related('product').order_by('name')
    context = {'categories': categories,}
    return render(request, 'catalogue/store_front.html', context)


def product(request, slug):
    product = Product.objects.get(slug=slug)
    return render(request, 'catalogue/product.html', {'product': product})

@login_required
def product_to_cart(request, id):
    user = request.user
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        order, created = Order.objects.get_or_create(user=user, status='Pending')

        OrderItem.objects.create(
            order = order,
            product = product,
            price = product.price,
        )
        return redirect('store:store')
 
    return render(request, 'catalogue/product.html', {'product': product})