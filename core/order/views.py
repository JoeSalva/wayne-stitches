from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import OrderItem, Order
from django.db.models import Prefetch

# Create your views here.

@login_required
def cart(request):
    orders = Order.objects.filter(user=request.user, status='Pending').first()
    cart = OrderItem.objects.select_related('product').filter(order=orders)
    return render(request, 'cart.html', {'cart':cart, 'order':orders,})

@login_required
def remove_from_cart(request, id):
    order = Order.objects.get(user=request.user, status='Pending')
    item = OrderItem.objects.select_related('product').filter(order=order).get(id=id)
    if request.method == 'GET':
        item.delete()
        return redirect('order:cart')
    return render(request, 'cart.html', {'item':item})

@login_required
def create_order(request, id):
    order = Order.objects.filter(status='Pending').get(id=id)
    items = OrderItem.objects.select_related('product').filter(order=order)
    if request.method == 'POST':
        for item in items:
            stock = item.product.stock # type:ignore
            stock.qty -= item.qty
            stock.units_sold += item.qty
            stock.save()
        order.status = 'Processing'
        order.save()
        return redirect('order:order_history')
    return render(request, 'cart.html', {'order':order})

@login_required    
def order_history(request):
    orders = Order.objects.filter(status='Processing').prefetch_related(
        Prefetch('items', queryset=OrderItem.objects.select_related('product'))
    ).order_by('-date_created')
    return render(request, 'order.html', {'orders':orders,})