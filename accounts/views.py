from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm

from django.urls import reverse_lazy

from django.contrib import messages

from django.views import generic

from .forms import SignUpForm

from core.models import Category,Type_category



class SignUp(generic.CreateView):
    form_class =  SignUpForm 
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
    
    

    
        

  