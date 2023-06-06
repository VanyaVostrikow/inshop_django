from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from Main.models import Product
from .cart import Cart
from .forms import CartAddProductForm
from Coupon.forms import CouponApplyForm

@require_POST
def cart_add(request, pk):
    print("SALAM", pk)
    cart = Cart(request)
    print
    id = pk
    print(id)
    product = get_object_or_404(Product, pk=pk)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('Cart:detail')

def cart_remove(request, pk):
    print("HELLO", pk)
    cart = Cart(request)
    product = get_object_or_404(Product, pk=pk)
    cart.remove(product)
    return redirect('Cart:detail')
def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
                            initial={'quantity': item['quantity'],
                            'update': True})
    coupon_apply_form = CouponApplyForm()
    return render(request,
                  'Cart/detail.html',
                  {'cart': cart,
                   'coupon_apply_form': coupon_apply_form,
                   })