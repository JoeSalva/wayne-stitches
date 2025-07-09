from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import OrderItem, Order

# Create your views here.

@login_required
def cart(request):
    orders = Order.objects.filter(user=request.user, status='Pending').first()
    cart = OrderItem.objects.select_related('product').filter(order=orders)
    return render(request, 'cart.html', {'cart':cart, 'order':orders,})

@login_required
def remove_from_cart(request, id):
    order = Order.objects.get(status='Pending')
    item = OrderItem.objects.select_related('product').filter(order=order).get(id=id)
    if request.method == 'GET':
        item.delete()
        return redirect('order:cart')
    return render(request, 'cart.html', {'item':item})