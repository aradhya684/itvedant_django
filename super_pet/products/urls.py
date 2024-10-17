from django.urls import path
from . import views


urlpatterns =[

    path('',views.ProductListView.as_view(),name="productspage"),
    path('drools/',views.drools,name="droolspage"),  
    path('whiskas/',views.whiskas,name="whiskaspage"),
    path("search",views.search,name="search"),
    path('<int:pk>/',views.ProductDetailView.as_view(),name="product_detail"),
    path("create-product/",views.ProductCreateView.as_view(), name="create-product"),
    path("update-product/<int:pk>/",views.ProductUpdateView.as_view(),name="update-product"),
    path("delete-product/<int:pk>/",views.ProductDeleteView.as_view(),name="delete-product")

]




