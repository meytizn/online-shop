from django.shortcuts import render , HttpResponse
from .models import Product
from django.shortcuts import render ,get_object_or_404,redirect
from django.db.models import Q
from django.contrib import messages



def home(request):
  products=Product.objects.all() #[5]
  context={'products':products}
  return render(request,'shop/index.html',context)



def product(request,pk):
  product=get_object_or_404(Product,pk=pk)
  return render(request,'shop/product.html',{'product':product})


# Create your views here.
