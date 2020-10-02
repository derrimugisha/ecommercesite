from django.urls import path, include

from django.contrib.auth import views

from .forms import LoginForm

from .views import (CheckOut,
                    Contact, Products,
                    Single, Terms,
                    ProductKids, ProductMen,
                    nav_bar_home,
                    nav_bar, nav_bar_contact,
                    image_page, nav_bar2,
                    HomeView, SuccessPage, NavLinks,
                    checkout, AddressForm, MensShow,
                    WomensShow, Accessories)

urlpatterns = [

    # path('',nav_bar_home,name='home'),
    path('', nav_bar_home, name='home'),
    path('checkout', CheckOut.as_view(), name='checkout'),
    path('contact', nav_bar_contact, name='contact'),
    path('products/<int:pk>', NavLinks, name='products'),
    # path('signup',SignUP.as_view(),name='signup'),
    path('login/', views.LoginView.as_view(form_class=LoginForm), name="login"),
    path('terms', Terms.as_view(), name='terms'),
    path('productkids', ProductKids.as_view(), name='product_k'),
    path('productmen', ProductMen.as_view(), name='product_m'),
    path('testers', nav_bar, name='tester'),
    path('single/<int:pk>', Single.as_view(), name='single'),
    path('successfull', SuccessPage.as_view(), name='successfull'),
    path('checkoutpreview', AddressForm.as_view(), name='checkoutpreview'),
    path('men/', MensShow.as_view(), name='men'),
    path('women/', WomensShow.as_view(), name='women'),
    path('accessories', Accessories.as_view(), name='accessories')



]
