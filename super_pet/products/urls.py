from django.urls import path
from . import views


urlpatterns =[

    path('',views.products,name="productspage"),
    path('drools/',views.drools,name="droolspage"),  
    path('whiskas/',views.whiskas,name="whiskaspage"),
    path("search",views.search,name="search")

]




