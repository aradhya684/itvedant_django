from django.db import models

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

    def __str__(self):
        return self.product_name

    product_name =  models.CharField(max_length=100,null=False)
    product_description = models.TextField(default="product description")
    product_price = models.PositiveIntegerField(default=0)
    product_image = models.ImageField(upload_to="products/")
    product_brand = models.CharField(max_length=100,default="superpet")

    aradhya = models.Manager() #if you want to change the name of manager in shell from objects to aradhya
    cust_manager = custom_manager()


class category(models.Model):
    pass

    # category_name=models.CharField(max_length=100,null=False)
    # category_description= models.TextField(default="product description")


# theory-part for shell querys
# Product.cust_manager.all().filter(product_price__gt=1500)  double underscore and gt means greater then 1500
# Product.cust_manager.all().filter(product_price__gte=1500)  double underscore and gte means greater then and equel to 1500

# Product.cust_manager.all().filter(product_price__lt=1500)  double underscore and lt means less then 1500
# Product.cust_manager.all().filter(product_price__lte=1500)  double underscore and lte means less then and equel to 1500

#Product.cust_manager.all().filter(product_name__contains="d") finds any product name which has 'd' in it, it is case-sensitive
#Product.cust_manager.all().filter(product_name__icontains="d") finds any product name which has 'd' in it but it is not case-sensitive

#Product.cust_manager.all().filter(product_name__startswith="d") finds any product name which stars with 'd' but is is case_sensitive
#Product.cust_manager.all().filter(product_name__istartswith="d") finds any product name which stars with 'd' but is is not case_sensitive

#Product.cust_manager.all().filter(product_name__endsswith="d") finds any product name which ends with 'd' but is is case_sensitive
#Product.cust_manager.all().filter(product_name__iendswith="d") finds any product name which ends with 'd' but is is not case_sensitive

#Product.cust_manager.all().filter(product_name__exact="Arden Grange dog food")
# finds product name which is given in query (finds exact match)

#Product.cust_manager.all().order_by('id') for asceding order
#Product.cust_manager.all().order_by('-id') for descding order

#Product.cust_manager.all().filter(product_price__range=(1000,2000)) to check range of any number like price

# Product.cust_manager.all().filter(id_in=(3,4,6)) to return multiple values use in opeartor





