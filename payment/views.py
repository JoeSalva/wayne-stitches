from django.shortcuts import render
import requests
from django.conf import settings
from django.shortcuts import redirect, render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from order.models import Order, OrderItem
from django.contrib.auth.decorators import login_required
from order.choices import DELIVERY_PRICES
import uuid


# Create your views here.
@login_required
def initiate_payment_page(request, id):
    order = get_object_or_404(Order, id=id, status=Order.DELI_STATUS.PENDING)
    items = OrderItem.objects.filter(order=order).select_related('product')
    saved_state = request.user.address.state
    delivery_fee = (DELIVERY_PRICES[saved_state])
    total_price = order.end_total_price

    return render(request, "payment/initiate.html", {'order': order, 'delivery_fee': delivery_fee, 'total_price': total_price, 'items':items})


@login_required
def initialize_payment(request, id):
    order = get_object_or_404(Order, id=id)
    total_price = order.end_total_price

    if request.method == "POST":
        email = request.user.email
        amount = float(total_price)
        tx_ref = str(uuid.uuid4())  # unique transaction reference

        headers = {
            "Authorization": f"Bearer {settings.FLUTTERWAVE_PUBLIC_KEY}",
            "Content-Type": "application/json",
        }

        payload = {
            "tx_ref": tx_ref,
            "amount": amount,
            "currency": "NGN",
            "redirect_url": request.build_absolute_uri(f"/payment/verify/{order.id}/"),
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
        print(res_data)

        if res_data["status"] == "success":
            payment_link = res_data["data"]["link"]
            return redirect(payment_link)
        else:
            return render(request, "error.html", {"message": res_data.get("message", "Payment initiation failed.")})
    return redirect("order:cart")

@login_required
def verify_payment(request, id):
    order = get_object_or_404(Order, id=id, status=Order.DELI_STATUS.PENDING)
    items = OrderItem.objects.select_related('product').filter(order=order)
    tx_ref = request.GET.get("tx_ref")
    transaction_id = request.GET.get("transaction_id")

    headers = {
        "Authorization": f"Bearer {settings.FLUTTERWAVE_SECRET_KEY}",
    }

    url = f"https://api.flutterwave.com/v3/transactions/{transaction_id}/verify"

    response = requests.get(url, headers=headers)
    res_data = response.json()

    if res_data["status"] == "success" and res_data["data"]["status"] == "successful" and res_data["data"]["tx_ref"] == tx_ref:
        for item in items:
            stock = item.product.stock # type:ignore
            stock.qty -= item.qty
            stock.units_sold += item.qty
            stock.save()
        order.status = Order.DELI_STATUS.PROCESSING
        order.save()
        return redirect('order:track_order', id=order.id)
    else:
        return render(request, "error.html", {"message": "Payment verification failed."})