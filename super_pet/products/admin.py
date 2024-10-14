from django.contrib import admin
from .models import Product #import every model

# Register your models here.


# admin.site.register(Product) #write this for every model 



class productinfo(admin.ModelAdmin):
    list_display =['id','product_name','product_brand','product_price'] #predefined variable do not write any other variable name
    

admin.site.register(Product,productinfo) 

#orm method is used to filter products use python shell