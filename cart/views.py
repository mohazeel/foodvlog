from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from store.models import *
from .models import *


# Create your views here.


def cart_details(request, tot=0, count=0, cart_item=None):
    try:
        ct = cartlist.objects.get(cart_id=c_id(request))
        cart_item = item.objects.filter(cart=ct, active=True)
        for i in cart_item:
            tot += (i.prod.price * i.quantity)
            count += i.quantity
    except ObjectDoesNotExist:
        pass
    return render(request, 'cart.html', {'ci': cart_item, 't': tot, 'cn': count})


def c_id(request):
    ct_id = request.session.session_key
    if not ct_id:
        ct_id = request.session.create()
    return ct_id


def add_cart(request, product_id):
    pass


def min_cart(request):
    pass


def cart_delete(request):
    pass
