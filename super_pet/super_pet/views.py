from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm

def home(request):
    return render(request,"index.html")


def contact(request):
    return render(request,"contact.html")


def about(request):
    return render(request,"about.html")

def login(request):
    return render(request,"login.html")


def register(request):
    if request.method=="GET":
        # form = UserCreationForm()
        form = CustomUserCreationForm 
        return render(request,"register.html",{"form":form})
    else:
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/login")
        return render(request,"register.html",{"form":form})

