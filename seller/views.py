from django.shortcuts import render

# Create your views here.
def seller_home(request):
    return render (request, 'seller/home.html')

def seller_addproduct(request):
    return render (request, 'seller/addproduct.html')

def seller_updatestock(request):
    return render (request, 'seller/updatestock.html')

def seller_productcatalog(request):
    return render (request, 'seller/productcatalog.html')

def seller_changepassword(request):
    return render (request, 'seller/changepassword.html')