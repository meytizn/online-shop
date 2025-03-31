from django.shortcuts import render , HttpResponse

def home(request):
  return render(request,'shop/index.html')



def product(request):
  return render(request,'shop/product.html')


# Create your views here.
