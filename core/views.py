from django.shortcuts import render

from django.views.generic import TemplateView,ListView,DetailView

from .models import (Type_category,Category,Product,)

import random



# from django.views.generic.base import View


def nav_bar_home(request):
    nav_query = Category.objects.select_related('type_id').all()

    product_pk = Product.objects.values_list('pk',flat=True)

    random_pk = random.choice(product_pk)

    accessories = Product.objects.all().select_related().filter(category_id = 1).order_by('?')[:1]

    women_show = Product.objects.all().select_related().filter(type_category_id=2)[:1]

    all_products = Product.objects.all().order_by('?')[:4]

    f_object = Product.objects.filter(pk = random_pk)

    results = nav_query.filter(type_id = '1')

    results2 = nav_query.filter(type_id = '2')

    results3 = nav_query.filter(type_id = '3')

    context = {'queryset':results,'queryset2':results2,
               'queryset3':results3,'banner':f_object,
               'accessories':accessories,'womenshow':women_show,
               'all_products':all_products
              }

    return render(request,"home.html",context)

class SuccessPage(TemplateView):
    template_name = 'successpay.html'
    

def nav_bar2(request):
    items = Product.objects.all()[:4]

    nav_query = Category.objects.select_related('type_id').all()

    product_pk = Product.objects.values_list('pk',flat=True)

    random_pk = random.choice(product_pk)

    accessories = Product.objects.all().select_related().filter(category_id = 1).order_by('?')[:1]

    women_show = Product.objects.all().select_related().filter(type_category_id=2)[:1]

    all_products = Product.objects.all().order_by('?')[:4]

    f_object = Product.objects.filter(pk = random_pk)

    results = nav_query.filter(type_id = '1')

    results2 = nav_query.filter(type_id = '2')

    results3 = nav_query.filter(type_id = '3')

   
    # f_object = items

    context = {'queryset':results,'queryset2':results2,
               'queryset3':results3,'banner':f_object,
               'accessories':accessories,'womenshow':women_show,
               'all_products':all_products
              }

    # context = {
    #     'banner':f_object,'queryset':results,
    # }
    return render(request,"tester.html",context)


def nav_bar_contact(request):
    nav_query = Category.objects.select_related('type_id').all()
    # TypeCategorySelector = Type_category.objects.all().filter(type_id = '1')
    results = nav_query.filter(type_id = '1')
    results2 = nav_query.filter(type_id = '2')
    results3 = nav_query.filter(type_id = '3')
    context = {'queryset':results,'queryset2':results2,
               'queryset3':results3}
    return render(request,"contact.html",context)





 
class CheckOut(TemplateView):

    template_name = 'checkout.html'

class Contact(TemplateView):

    template_name = 'contact.html'

class Products(TemplateView):

    template_name = 'products.html'

# class SignUP(TemplateView):

#     template_name = 'signup.html'

# class LogIn(TemplateView):

#     template_name = 'login.html'

class Single(DetailView):

    model = Product

    template_name= 'single.html'

    def get_context_data(self,*args,**kwargs):
        context = super(Single,self).get_context_data(*args,**kwargs)
        queryset = Product.objects.all().order_by('?')[:4]
        context["category"] = queryset
        return context



class Terms(TemplateView):

    template_name = 'terms.html'

class ProductKids(TemplateView):

    template_name = 'product_k.html'


class ProductMen(TemplateView):

    template_name = 'product_m.html'

def nav_bar(request):
    items = Product.objects.all()[:4]

    f_object = items

    context = {
        'banner':f_object,'rew':'sdgdsd'
    }
    return render(request,"tester.html",context)
    

class  image_page(ListView):
    model = Product
    template_name = 'tester.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.all().order_by('?')[:2]

class HomeView(ListView):
    template_name = 'tester.html'
    
    def get_queryset(self):
        products = Product.objects.all().order_by('?')[:2]
        context = {'products':products}
        return products 









