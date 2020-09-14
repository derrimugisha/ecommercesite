from django import forms
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Sign Up Form
class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')

    class Meta:
        model = User
        fields = [
            'username',
            'email', 
            'password1', 
            'password2', 
            ]

    # def show_links(request):
    #     nav_query = Category.objects.select_related('type_id').all()
    #     # TypeCategorySelector = Type_category.objects.all().filter(type_id = '1')
    #     results = nav_query.filter(type_id = '1')
    #     results2 = nav_query.filter(type_id = '2')
    #     results3 = nav_query.filter(type_id = '3')
    #     context = {'queryset':results,'queryset2':results2,'queryset3':results3}
    #     return render(request,"signup.html",context)