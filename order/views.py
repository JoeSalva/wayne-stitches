from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import OrderItem, Order
from decimal import Decimal
from django.db.models import Prefetch
from .forms import DeliveryForm
from .choices import NigerianStates, DELIVERY_PRICES


# Create your views here.

@login_required
def cart(request):
    order = Order.objects.filter(user=request.user, status=Order.DELI_STATUS.PENDING).first() #type: ignore
    cart = OrderItem.objects.select_related('product').filter(order=order)
    delivery_fee = DELIVERY_PRICES[request.user.address.state]
    total_price = sum(item.qty * item.price for item in cart )
    total_price += delivery_fee
    return render(request, 'cart.html', {'cart':cart, 'order':order, 'fee':delivery_fee, 'total': total_price})

@login_required
def remove_from_cart(request, id):
    order = Order.objects.get(user=request.user, status=Order.DELI_STATUS.PENDING) #type: ignore
    item = OrderItem.objects.select_related('product').filter(order=order).get(id=id)
    if request.method == 'GET':
        item.delete()
        return redirect('order:cart')
    return render(request, 'cart.html', {'item':item})

@login_required
def create_order(request, id):
    order = get_object_or_404(Order, id=id, status=Order.DELI_STATUS.PENDING)
    if request.method == 'POST':
        items = OrderItem.objects.select_related('product').filter(order=order)
        user = request.user
        saved_state = user.address.state
        total_price = sum(item.qty * item.price for item in items )
        total_price += DELIVERY_PRICES[saved_state]
        order.end_total_price = Decimal(total_price)
        order.delivery_fee = DELIVERY_PRICES[saved_state]
        order.delivery_state = saved_state
        order.save()
        return redirect('payment:initiate_payment', id=order.id) #type:ignore
    return render(request, 'cart.html', {'order':order,})

def view_form(request):
    user = request.user
    saved_state = user.address.state
    form = DeliveryForm(initial={'delivery_state': saved_state})
    return render(request, 'form_check.html', {'form': form})

@login_required    
def order_history(request):
    orders = Order.objects.filter(user = request.user, status=Order.DELI_STATUS.PROCESSING).prefetch_related(
        Prefetch('items', queryset=OrderItem.objects.select_related('product'))
    ).order_by('-date_created')
    return render(request, 'order.html', {'orders':orders,})

@login_required
def track_order(request, id):
    order = get_object_or_404(Order, id=id)
    context = {
        "order": order,
        "is_pending": order.status == Order.DELI_STATUS.PENDING,
        "is_processing": order.status == Order.DELI_STATUS.PROCESSING,
        "is_delivered": order.status == Order.DELI_STATUS.DELIVERED,
    }
    return render(request, 'track_order.html', context)


# for item in items:
#             stock = item.product.stock # type:ignore
#             stock.qty -= item.qty
#             stock.units_sold += item.qty
#             stock.save()
#         order.status = Order.DELI_STATUS.PROCESSING #type: ignore
#         order.delivery_state = saved_state