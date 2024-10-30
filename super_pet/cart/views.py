from django.shortcuts import render,HttpResponseRedirect

# Create your views here.


def add_to_cart(request,productID):
    # print("*********************",productID,"********************")
    # print("*********************",request.user,"*****************")
    currentUser = request.user
    return HttpResponseRedirect("/products")
    


def show_cart(request):
    return render(request,'cart.html')

