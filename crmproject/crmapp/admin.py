from django.contrib import admin
from .models import Customer,Product,Order

class adminCustomer(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','address','location','mobile','create_date']
class adminProduct(admin.ModelAdmin):
    list_display = ['name','price','description','order_date','category']
class adminOrder(admin.ModelAdmin):
    list_display = ['customer','product','status']


admin.site.register(Customer,adminCustomer)
admin.site.register(Product,adminProduct)
admin.site.register(Order,adminOrder)
