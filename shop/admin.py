from django.contrib import admin

from .models import Product,Order,OrderItem,Invoice,Transaction


class ProductAdmin(admin.ModelAdmin):
    list_display=['name','created_time'] 


class OrderAdmin(admin.ModelAdmin):
    list_display=['id','customer','order_date']


class OrderItemAdmin(admin.ModelAdmin):
    list_display=['id','order','product']


class TransactionAdmin(admin.ModelAdmin):
    list_display=['id','Invoice','amount','transaction_date','status']   #pin has error dict in model


class InovoiceAdmin(admin.ModelAdmin):
    list_display=['id','order' ]



admin.site.register(Product,ProductAdmin)  
admin.site.register(Order,OrderAdmin) #customers
admin.site.register(OrderItem,OrderItemAdmin)  #get user and a price 
admin.site.register(Invoice,InovoiceAdmin) #Factor
admin.site.register(Transaction,TransactionAdmin) #paymentstatus

# Register your models here.
