from django.urls import path
from . import views


urlpatterns =[

    path('',views.ProductListView.as_view(),name="productspage"),
    path('drools/',views.drools,name="droolspage"),  
    path('whiskas/',views.whiskas,name="whiskaspage"),
    path("search",views.search,name="search"),
    path('<int:pk>/',views.ProductDetailView.as_view(),name="product_detail")

]




