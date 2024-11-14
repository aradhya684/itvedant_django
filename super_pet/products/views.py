from django.shortcuts import render
from .models import Product, Categories
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
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

#this is list view import above
class ProductListView(ListView):
    model = Product #keep this variable this is default variable, here Product is our model name 

#this is detail view import above
class ProductDetailView(DetailView):
    model = Product #keep this variable this is default variable, here Product is our model name  
    template_name = 'products/productdetails.html'

#this is create view import above

@method_decorator(staff_member_required,name = "dispatch")
class ProductCreateView(CreateView):
    model = Product
    fields="__all__"
    success_url = "/products"

 #this is update view import above
@method_decorator(staff_member_required,name = "dispatch")
class ProductUpdateView(UpdateView):
    model = Product
    fields="__all__"
    success_url = "/products"

@method_decorator(staff_member_required,name = "dispatch")
class ProductDeleteView(DeleteView):
    model = Product
    success_url = "/products"



class CategoryDetailView(DetailView):
    model = Categories #keep this variable this is default variable, here Product is our model name  
    template_name = 'category/category_details.html'
    slug_field = "category_slug"
    context_object_name = "category_obj"


    