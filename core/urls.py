from django.urls import path,include

from .views import (CheckOut, 
                      Contact,Products,
                      Single,Terms,
                      ProductKids,ProductMen,
                      nav_bar_home,
                      nav_bar,nav_bar_contact,
                      image_page,nav_bar2,
                      HomeView,SuccessPage,)

urlpatterns = [

    # path('',nav_bar_home,name='home'),
    path('',nav_bar_home,name='home'),
    path('checkout',CheckOut.as_view(),name='checkout'),
    path('contact',nav_bar_contact,name='contact'),
    path('products',Products.as_view(),name='product'),
    # path('signup',SignUP.as_view(),name='signup'),
    # path('login',LogIn.as_view(),name='login'),
    path('terms',Terms.as_view(),name='terms'),
    path('productkids',ProductKids.as_view(),name='product_k'),
    path('productmen',ProductMen.as_view(),name='product_m'),
    path('testers',nav_bar,name='tester'),
    path('single/<int:pk>',Single.as_view(),name='single'),
    path('successfull',SuccessPage.as_view(),name='successfull')
    # path('single/<int:pk>',AllSingle.as_view(),name='allsingle'),
    
    
]