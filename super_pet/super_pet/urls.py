"""
URL configuration for super_pet project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from . import views #here dot . means same package or file not form another folder
from products import urls #adding urls.py from products applicatiom
from cart import urls #adding urls.py from cart application
from . import settings #here dot . means same package or file not form another folder



urlpatterns = [

    path("admin/",admin.site.urls),
    path('', views.home, name="homepage"),
    path('profile/',views.profile,name="profilepage"),
    path('about/',views.about,name="aboutpage"),
    path('login/',views.login_user,name="loginpage"),
    path('logout/',views.logout_user,name="logoutpage"),
    path('register/',views.register,name="registerpage"),
    path('adminportal/',views.admin,name="adminportal"),
    path('products/',include('products.urls')),
    path('cart/',include('cart.urls'))

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)







