from django.shortcuts import render
from .models import Products

# Create your views here.
def home(request):
    products=Products.objects.all()
    return render(request, 'home.html',{'products':products})