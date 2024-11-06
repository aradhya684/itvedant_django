"""
URL configuration for start_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from firstapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='homepage'),
    path('about-page/',views.about),
    path('first-page/',views.firstrequest),
    path('second-page/',views.secondrequest),
    path('third-page/',views.thirdrequest),
    path('courses/',views.courses),
    path('file1/',views.page_2),
    path('file2/',views.page_3),
    path('students/',views.students,name='studentpage'),
    path('office/',views.office),
    path('book/',views.book,name='book'),
    path('product/',views.product,name='product'),
    path('employee/',views.employee),
    path('cbv/',views.myview.as_view(),name="cbv"),
    path('learnfilters/',views.learnfilters,name="filters")
]
