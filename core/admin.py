from django.contrib import admin

from .models import Type_category,Category,Product,Address

class ProductAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = [ 'productname', 'price']

admin.site.register(Type_category)

admin.site.register(Category)

admin.site.register(Product,ProductAdmin)

admin.site.register(Address)
 