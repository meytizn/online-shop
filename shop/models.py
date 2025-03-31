from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

class Product(models.Model):
    name = models.CharField( max_length=100)
    description=models.TextField()
    created_time=models.DateTimeField(auto_now_add=True)
    updated_time=models.DateTimeField( auto_now=True)
    image=models.ImageField(upload_to='store/images/product/%y/%m/%d',default='news/images/1.png',blank=True)
    price=models.DecimalField( max_digits=10, decimal_places=0)

    class Meta:
        ordering=('created_time')
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("shop:product", args=[self.id])






class Order(models.Model):
    customer=models.ForeignKey(User, on_delete=models.CASCADE)
    order_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id
    
    






class OrderItem(models.Model):
    order=models.ForeignKey(Order, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.SET_NULL,null=True)
    product_price=models.DecimalField( max_digits=10, decimal_places=0)
    product_count=models.PositiveIntegerField()
    product_cost=models.DecimalField( max_digits=10, decimal_places=0)

    def __str__(self):
        return self.id



class Invoice(models.Model):
    order=models.ForeignKey(Order, on_delete=models.SET_NULL,null=True)
    invoice=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id




class Transaction(models.Model):
    STATUS_CHOICES=(
        ('pending','pending'),
        ('failed','failed'),
        ('completed','completed'),
    )
    Invoice=models.ForeignKey(Invoice, on_delete=models.SET_NULL,null=True)
    transaction_date=models.DateTimeField(auto_now_add=True)
    amount=models.DecimalField( max_digits=10, decimal_places=0)
    status=models.CharField( max_length=10,choices= STATUS_CHOICES,default='pending')

    def __str__(self):
        return self.id


# Create your models here.
