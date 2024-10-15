from django.shortcuts import render
from .models import Product
from django.views.generic import ListView,DetailView


# Create your views here.
#this is function based views
def products(request):
    return render(request,"products.html")


def drools(request):
    p1=Product.cust_manager.drools()
    return render(request,"products.html", {"products":p1})

def whiskas(request):
    p2=Product.cust_manager.whiskas()
    return render(request,"products.html", {"products":p2})

def search(request):
    keyword = request.GET.get("keyword")
    product = Product.cust_manager.all().filter(product_name__icontains = keyword)
    return render(request,"products.html", {"products":product})

class ProductListView(ListView):
    model = Product #keep this variable this is default variable


class ProductDetailView(DetailView):
    model = Product #keep this variable this is default variable
    template_name = 'products/productdetails.html'


    



