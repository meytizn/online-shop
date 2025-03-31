from django.shortcuts import render , HttpResponse
from .models import Product


def home(request):
  products=Product.objects.all() #[5]
  context={'products':products}
  return render(request,'shop/index.html',context)



def product(request):
  return render(request,'shop/product.html')


# Create your views here.
