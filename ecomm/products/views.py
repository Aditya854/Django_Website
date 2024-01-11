from pydoc import render_doc
from tkinter import E
from django.shortcuts import redirect, render
from products.models import Product
# from accounts.models import Cart, CartItem
from accounts.models import Cart, CartItem


def get_product(request , slug):
    try:
        product = Product.objects.get(slug =slug)
        context = {'product':product}
        if request.GET.get('size'):
            size = request.GET.get('size')
            print(size)
            price = product.get_product_price_by_size(size)
            context['selected_size'] = size
            context['updated_price'] = price
        
        
        
        return render(request  , 'product/product.html' , context = context)

    except Exception as e:
        print(e)

    def add_to_cart(request, slug):
        variant = request.GET.get('variant')
        product = Product.objects.get(slug=slug)
        user  = request.user
        cart , _ = Cart.objects.get_or_create(user = user , is_paid=False)

        return redirect('/')