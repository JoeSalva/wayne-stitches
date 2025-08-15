from django.conf import settings
from django.shortcuts import render, redirect
import requests
from django.contrib.auth.decorators import login_required
from .models import OrderItem, Order
from decimal import Decimal
from django.db.models import Prefetch
from .forms import DeliveryForm
from .choices import NigerianStates, DELIVERY_PRICES
from django.views.decorators.csrf import csrf_exempt
import uuid

# Create your views here.

@login_required
def cart(request):
    order = Order.objects.filter(user=request.user, status=Order.DELI_STATUS.PENDING).first() #type: ignore
    cart = OrderItem.objects.select_related('product').filter(order=order)
    delivery_fee = DELIVERY_PRICES[request.user.address.state]
    return render(request, 'cart.html', {'cart':cart, 'order':order, 'fee':delivery_fee})

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
    order = Order.objects.filter(status=Order.DELI_STATUS.PENDING).get(id=id)
    items = OrderItem.objects.select_related('product').filter(order=order)
    user = request.user
    saved_state = user.address.state
    # form = DeliveryForm(initial={'delivery_state': saved_state})
    total_price = sum(item.qty * item.price for item in items )
    total_price_with_delivery = total_price + DELIVERY_PRICES[saved_state]
    if request.method == 'POST':
        order.end_total_price += Decimal(total_price)
        for item in items:
            stock = item.product.stock # type:ignore
            stock.qty -= item.qty
            stock.units_sold += item.qty
            stock.save()
        order.status = Order.DELI_STATUS.PROCESSING #type: ignore
        order.delivery_state = saved_state
        order.delivery_fee = DELIVERY_PRICES[saved_state]
        order.save()
        return redirect('order:order_history')
    return render(request, 'cart.html', {'order':order, 'overall_total': total_price_with_delivery})

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

def initialize_payment(request):
    if request.method == "POST":
        email = request.POST.get("email")
        amount = request.POST.get("amount")
        tx_ref = str(uuid.uuid4())

        headers = {
            "Authorization": f"Bearer {settings.FLUTTERWAVE_SECRET_KEY}",
            "Content-Type": "application/json",
        }

        payload = {
            "tx_ref": tx_ref,
            "amount": amount,
            "currency": "NGN",
            "redirect_url": request.build_absolute_uri("/order/payment/verify/"),
            "payment_options": "card,ussd,banktransfer",
            "customer": {
                "email": email,
            },
            "customizations": {
                "title": "Wayne Stitches",
                "description": "Payment for items in cart",
                "logo": "https://res.cloudinary.com/dokhpnmjw/image/upload/v1755011837/logo_bstzwo.png"
            }
        }

        response = requests.post("https://api.flutterwave.com/v3/payments", json=payload, headers=headers)
        res_data = response.json()

        if res_data["status"] == "success":
            payment_link = res_data["data"]["link"]
            return redirect(payment_link)
        else:
            return render(request, "error.html", {"message": res_data.get("message", "Payment initiation failed.")})

    return render(request, "initiate.html")

def verify_payment(request):
    tx_ref = request.GET.get("tx_ref")
    transaction_id = request.GET.get("transaction_id")

    headers = {
        "Authorization": f"Bearer {settings.FLUTTERWAVE_SECRET_KEY}",
    }

    url = f"https://api.flutterwave.com/v3/transactions/{transaction_id}/verify"

    response = requests.get(url, headers=headers)
    res_data = response.json()

    if res_data["status"] == "success" and res_data["data"]["status"] == "successful" and res_data["data"]["tx_ref"] == tx_ref:
        # Payment was successful
        return render(request, "success.html", {"data": res_data["data"]})
    else:
        return render(request, "error.html", {"message": "Payment verification failed."})