from django.shortcuts import render,HttpResponse
from django.views import View #for class based views

# Create your views here.

#function based view

def about(request):
    return HttpResponse("about page")

def home(request):
    return HttpResponse("home page")


def firstrequest(request):
    return HttpResponse("this is first request")


def secondrequest(request):
    return HttpResponse("this is second request")


def thirdrequest(request):
    return HttpResponse("this is third request")


def courses(request):
    return render(request,"courses.html",{})

def page_2(request):
    return render(request,"file_1.html",{})

def page_3(request):
    return render(request,"file_2.html",{})

def students(request):
    print("**************************")
    print(request.method)
    print("**************************")
    context={"id":101,"name":"aradhya","home":"prabhadevi","subjects":["physics","chemistry","biology","maths","english","hindi"]}
    return render(request,"students.html",context)

def book(request):
    # print(request.GET.get("bookname"))
    # print(request.GET.get("bookprice"))
    context={"BookName":request.GET.get("bookname"),
            "BookPrice":request.GET.get("bookprice")}
    return render(request,"book.html",context)


def office(request):
    
    context={"id":102,"name":"aradhya","role":"data scientist","branch":["mumbai","pune","delhi"]}
    return render(request,"office.html",context)

def product(request):

    context={"ProductName":request.GET.get("productname"),
            "ProductPrice":request.GET.get("productprice")}
    return render(request,"product.html",context)



def employee(request):
    if request.method=='GET':
        return render(request,"employee.html")
    if request.method=="POST":
        context=request.POST.get("empname")
        return render(request,"employee.html",{"emPname":context})



def learnfilters(request):
        return render(request,"newfile.html",{"data":"dJaNgO"})
    

#class based views
#class based views
#class based views 
#class based views

class myview(View):
    def get(self,request):
        return render(request,"my_view.html")
        
    
    def post(self,request):
        return render(request,"success.html")
   


