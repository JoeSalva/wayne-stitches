from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category
from order.models import OrderItem, Order
from .forms import EditProductForm

# Create your views here.

def store_front(request):
    is_vendor = request.user.groups.filter(name='Vendor').exists()
    categories = Category.objects.prefetch_related('product').order_by('name')
    context = {'categories': categories, 'is_vendor': is_vendor}
    return render(request, 'catalogue/store_front.html', context)


def product(request, slug):
    product = Product.objects.get(slug=slug)
    return render(request, 'catalogue/product.html', {'product': product})

def category_view(request, slug):
    category = Category.objects.prefetch_related('product').get(slug=slug)
    products = category.product.all()  # type: ignore
    return render(request, 'catalogue/category.html', {'category': category, 'products':products})


# def to_edit_product(request, slug):
#     product = Product.objects.get(slug=slug)
#     return render(request, 'catalogue/edit_product.html', {'product': product})

@login_required
def edit_product(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        ep_form = EditProductForm(request.POST, request.FILES, instance=product)
        if ep_form.is_valid():
            ep_form.save()
            return redirect('store:edit_product', id=product.id) # type:ignore
    else:
            ep_form = EditProductForm(instance=product)
    return render(request, 'catalogue/edit_product.html', {'form': ep_form})
        
@login_required
def product_to_cart(request, id):
    user = request.user
    product = Product.objects.get(id=id)
    qty = int(request.POST.get('qty'))
    if request.method == 'POST':
        order, created = Order.objects.get_or_create(user=user, status=Order.DELI_STATUS.PENDING)
        order_item, item_created = OrderItem.objects.get_or_create(
            order = order,
            product = product,
            defaults={'price':product.price, 'qty':qty}
        )

        if not item_created:
            order_item.qty += qty
            order_item.save()

        return redirect('store:store')
 
    return render(request, 'catalogue/product.html', {'product': product})