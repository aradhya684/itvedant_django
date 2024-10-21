from django.db import models
from autoslug import AutoSlugField


class Categories(models.Model):
    category_name = models.CharField(max_length=100,null=False)
    category_slug = AutoSlugField(populate_from='category_name',unique=True)



# Create your models here...

#object relational mapping

#step one we create class which inherits model class from models

# creating a custome manager in shell
# deciding output on 'all' query// making custom manager


class custom_manager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()
    
    def drools(self):
        return super().get_queryset().filter(product_brand='Drools')
    
    def whiskas(self):
        return super().get_queryset().filter(product_brand='Whiskas')
 


class Product(models.Model):

    # def __str__(self):
    #     return self.product_name

    product_name =  models.CharField(max_length=100,null=False)
    product_description = models.TextField(default="product description")
    product_price = models.PositiveIntegerField(default=0)
    product_image = models.ImageField(upload_to="products/")
    product_brand = models.CharField(max_length=100,default="superpet")

    aradhya = models.Manager() #if you want to change the name of manager in shell from objects to aradhya
    cust_manager = custom_manager()



  