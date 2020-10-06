from django.shortcuts import render
from . import views
 
# Create your views here.
def Home(request):
    return render(request,'frontend/Home.html')

def bread(request):
    return render(request,'frontend/bread.html')

def cake(request):
    return render(request,'frontend/cake.html')

def cookies(request):
    return render(request,'frontend/cookies.html')

def contact(request):
    return render(request,'frontend/contact.html')