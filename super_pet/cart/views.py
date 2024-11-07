from django.shortcuts import render,HttpResponseRedirect
from .models import cart,CartItem,Order
from products.models import Product
from .forms import orderform
import uuid
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
    cart_items = user_cart.cartitem_set.all() #here cartitem in our model name it is converted into lowercase from uppercase
    total = 0
    for i in cart_items:
        total += i.quantity*i.products.product_price
    return render(request,'cart.html',{"cart_items":cart_items,"total":total})


def update_cartitem(request,pk):
    cartitem = CartItem.objects.get(id = pk)
    cartitem.quantity = int(int(request.GET.get('quantity')))
    cartitem.save()
    
    return HttpResponseRedirect("/cart")


def delete_cartitem(request,pk):
    cartitem = CartItem.objects.get(id = pk)
    cartitem.delete()
    return HttpResponseRedirect("/cart")


def checkout(request):
    if request.method == 'GET':
        form = orderform()
        return render(request,"checkout.html",{"form":form})
    if request.method == 'POST':
        form = orderform(request.POST)
        print("valid??",form.is_valid())
        if form.is_valid():
            print(form.cleaned_data)
            Order.objects.create(order_id = uuid.uuid4().hex,
                                  user = request.user,
                                    address_line_1 = form.cleaned_data["address_line_1"],
                                     address_line_2 = form.cleaned_data["address_line_2"],
                                      city = form.cleaned_data['city'], 
                                      state = form.cleaned_data['state'], 
                                      pincode = form.cleaned_data['pincode'], 
                                      phone_no = form.cleaned_data['phone_no'])
    return HttpResponseRedirect("/cart/checkout/")

