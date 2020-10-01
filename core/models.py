from django.db import models

from django.urls import reverse

from django.contrib.auth.models import User

class Type_category(models.Model):
    typename = models.CharField(max_length= 255)

    def __str__(self):
        return self.typename

class Category(models.Model):
    type_id = models.ForeignKey(Type_category,on_delete=models.CASCADE)
    category_name = models.CharField(max_length= 255)

    def __str__(self):
        return self.category_name

class Product(models.Model):
    productname = models.CharField(max_length=255)
    type_category_id = models.ForeignKey(Type_category,on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category,on_delete=models.CASCADE)
    size = models.CharField(max_length=500)
    colors = models.CharField(max_length=500)
    product_description = models.TextField()
    price = models.CharField(max_length=255)
    quantit = models.CharField(max_length=255)
    discount = models.CharField(max_length=255,default=0)
    ranking = models.CharField(max_length=255, blank=True)
    picture = models.ImageField(upload_to='images')

    def __str__(self):
        ret = self.productname + ',' + self.price + ',' 
        
        return ret

    # def get_absolute_url(self):
    #     return reverse('single',args=[str(self.id)])

class Address(models.Model):
    user = models.CharField(max_length=255,)
    country = models.CharField(max_length=255,default="Uganda")
    district = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    streetaddress = models.CharField(max_length=255,blank=True)
    apartmentaddress = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.user
		


