from django.urls import path
from . import views


urlpatterns =[

path("",views.show_cart,name = "showcart"),
path("add-to-cart/<int:productID>/",views.add_to_cart,name = "addtocart")

]


