from django.shortcuts import render,HttpResponseRedirect
from .models import cart,CartItem
from products.models import Product

# Create your views here.


def add_to_cart(request,productID):
    # print("*********************",productID,"********************")
    # print("*********************",request.user,"*****************")
    currentUser = request.user
    cart_obj,created = cart.objects.get_or_create(user = currentUser) #name of varible and model should not be same
    cartitem,created = CartItem.objects.get_or_create(cart = cart_obj,products = Product.cust_manager.get(id = productID))
    product_quantity = int(request.GET.get('quantity'))
    if created:
        cartitem.quantity = product_quantity
    else:
        cartitem.quantity = cartitem.quantity + product_quantity
    
    cartitem.save()
    return HttpResponseRedirect("/products")
    

def show_cart(request):
    currentUser = request.user
    user_cart = cart.objects.get(user = currentUser)
    cart_items = user_cart.cartitem_set.all() #here cartitem in our model name it is converted into lowercase form uppercase
    total = 0
    for i in cart_items:
        total += i.quantity*i.products.product_price
    return render(request,'cart.html',{"cart_items":cart_items,"total":total})

