from django.shortcuts import render , HttpResponse

def home(request):
  return render(request,'shop/home.html')

# Create your views here.
