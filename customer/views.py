from django.shortcuts import render


# Create your views here.
def customer_home(request):
    return render (request, 'customer/customer_home.html')

def customer_product(request):
    return render (request, 'customer/product_details.html')

def customer_cart(request):
    return render (request, 'customer/cart.html')
    
def customer_myorder(request):
    return render (request, 'customer/myorder.html')

def customer_changepassword(request):
    return render (request, 'customer/changepassword.html')    

  