from django.urls import path
from . import views


urlpatterns =[

path("",views.show_cart,name = "showcart"),
path("add-to-cart/<int:productID>/",views.add_to_cart,name = "addtocart"),
path("update-cart/<int:pk>/",views.update_cartitem,name = "update-cart-item"),
path("delete-cart/<int:pk>/",views.delete_cartitem,name = "delete-cart-item"),
path("checkout/",views.checkout,name = "checkcout")

]


