from django.shortcuts import render

from django.views.generic import TemplateView, ListView, DetailView

from django.views.generic.edit import CreateView

from .models import (Type_category, Category, Product, Address)

import random

from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin

# from django.views.generic.base import View


def nav_bar_home(request):
    nav_query = Category.objects.select_related('type_id').all()

    product_pk = Product.objects.values_list('pk', flat=True)

    random_pk = random.choice(product_pk)

    accessories = Product.objects.all().select_related().filter(
        category_id=1).order_by('?')[:1]

    women_show = Product.objects.all().select_related().filter(
        type_category_id=2)[:1]

    all_products = Product.objects.all().order_by('?')[:8]

    f_object = Product.objects.filter(pk=random_pk)

    results = nav_query.filter(type_id='1')

    results2 = nav_query.filter(type_id='2')

    results3 = nav_query.filter(type_id='3')

    context = {'queryset': results, 'queryset2': results2,
               'queryset3': results3, 'banner': f_object,
               'accessories': accessories, 'womenshow': women_show,
               'all_products': all_products
               }

    return render(request, "home.html", context)


class SuccessPage(TemplateView):
    template_name = 'successpay.html'


def nav_bar2(request):
    items = Product.objects.all()[:4]

    nav_query = Category.objects.select_related('type_id').all()

    product_pk = Product.objects.values_list('pk', flat=True)

    random_pk = random.choice(product_pk)

    accessories = Product.objects.all().select_related().filter(
        category_id=1).order_by('?')[:1]

    women_show = Product.objects.all().select_related().filter(
        type_category_id=2)[:1]

    all_products = Product.objects.all().order_by('?')[:4]

    f_object = Product.objects.filter(pk=random_pk)

    results = nav_query.filter(type_id='1')

    results2 = nav_query.filter(type_id='2')

    results3 = nav_query.filter(type_id='3')

    # f_object = items

    context = {'queryset': results, 'queryset2': results2,
               'queryset3': results3, 'banner': f_object,
               'accessories': accessories, 'womenshow': women_show,
               'all_products': all_products
               }

    # context = {
    #     'banner':f_object,'queryset':results,
    # }
    return render(request, "tester.html", context)


def nav_bar_contact(request):
    nav_query = Category.objects.select_related('type_id').all()
    # TypeCategorySelector = Type_category.objects.all().filter(type_id = '1')
    results = nav_query.filter(type_id='1')
    results2 = nav_query.filter(type_id='2')
    results3 = nav_query.filter(type_id='3')
    context = {'queryset': results, 'queryset2': results2,
               'queryset3': results3}
    return render(request, "contact.html", context)


def NavLinks(request, pk):
    nav_query = Category.objects.select_related('type_id').all()

    results = nav_query.filter(type_id='1')

    results2 = nav_query.filter(type_id='2')

    results3 = nav_query.filter(type_id='3')

    items = Product.objects.all().select_related().filter(category_id=pk).order_by('?')

    s_products = items

    context = {'filtcategory': s_products, 'queryset': results,
               'queryset2': results2, 'queryset3': results3}

    return render(request, "products.html", context)


class Single(DetailView):

    model = Product

    template_name = 'single.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Single, self).get_context_data(*args, **kwargs)
        queryset = Product.objects.all().order_by('?')[:4]
        context["category"] = queryset
        return context


class AddressForm(LoginRequiredMixin, CreateView):

    model = Address
    template_name = "checkoutpreview.html"
    fields = '__all__'

    login_url = 'login'


class MensShow(TemplateView):

    template_name = "product_m.html"

    def get_context_data(self, *args, **kwargs):
        context = super(MensShow, self).get_context_data(*args, **kwargs)
        myquery = Product.objects.all().select_related().filter(
            type_category_id=1).order_by('?')
        context['men'] = myquery
        return context


class WomensShow(TemplateView):
    template_name = 'product_w.html'

    def get_context_data(self, *args, **kwargs):
        context = super(WomensShow, self).get_context_data(*args, **kwargs)
        myquery = Product.objects.all().select_related().filter(
            type_category_id=2).order_by('?')
        context['women'] = myquery
        return context


class Accessories(TemplateView):
    template_name = 'accessories.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Accessories, self).get_context_data(*args, **kwargs)
        myquery = Product.objects.all().select_related().filter(
            type_category_id=3).order_by('?')
        context['accessories'] = myquery
        return context


@login_required
def checkout(request):

    print('*****'*30)
    print('the test is on')
    print('*****'*30)

    return render(request, "tester.html")


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
        'banner': f_object, 'rew': 'sdgdsd'
    }
    return render(request, "tester.html", context)


class image_page(ListView):
    model = Product
    template_name = 'tester.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.all().order_by('?')[:2]


class HomeView(ListView):
    template_name = 'tester.html'

    def get_queryset(self):
        products = Product.objects.all().order_by('?')[:2]
        context = {'products': products}
        return products


def NavLinkstest(request):
    items = Product.objects.all().select_related().filter(category_id=1).order_by('?')
    s_products = items
    context = {'filtcategory': s_products}
    return render(request, "tester.html", context)
