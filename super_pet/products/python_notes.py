
    # foreign key to achieve one to one relationship
    # oneToOneField() to achieve one to many relationship
    # manyToManyField() to achieve many to many relationship


# product = Product.aradhya.get(id=2) to get product with id 2
# product.product_name = "whiskas fish food" to chagnge teh name of the product
# product.save() to save the change in database table

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

#Product.cust_manager.all().filter(id_in=(3,4,6)) to return multiple values use in opeartor

#we use autoslug method to create links using slug method we need to install auto slug using pip install method

#Q objects (and ,or, not operator)

# for and operator we use&
# for or operator we use |
# for not operator we use ~

#  to write multiple querys in objects manager using and, or, not operator 
# filter(Q(product_name__istartswith="a") & Q(product_price__lte=5000))

# to import Q object we need to import it in python shell -- from django.db.modes import Q 

 #here we are using and operator using Q objects we are looking for products that starts with 
#"d" and price is less then 4000
 #Product.aradhya.all().filter(Q(product_name__istartswith="d") & Q(product_price__lte=4000)) 



 #here we are using or operator using Q objects we are looking for products that starts with 
#"d" or products that starts with "f"
 #Product.aradhya.all().filter(Q(product_name__istartswith="d") | Q(product_name__istartswith="f")) 


 #Product.aradhya.all().filter(Q(product_brand="Royal Canin") & Q(product_price__gt=5000)) 


#here we are looking for all brands but not royal canin so we are going to use not operator here

 #Product.aradhya.all().filter(~Q(product_brand="Royal Canin")) 


