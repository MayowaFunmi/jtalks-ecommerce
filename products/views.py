from django.shortcuts import render, get_object_or_404
from .cart import Cart
from .forms import CartAddProductForm
from .models import Product


def product_detail(request, id, slug):
    cart = Cart(request)
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'override': True})
    return render(request, 'products/details.html', {
        'product': product,
        'cart_product_form': cart_product_form,
        'cart': cart
    })
