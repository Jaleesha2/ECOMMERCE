from django.shortcuts import render

# Create your views here.
def common_customer_login(request):
    return render (request, 'common/customer_login.html')

def common_customer_signup(request):
    return render (request, 'common/customer_signup.html')

def common_project_home(request):
    return render (request, 'common/project_home.html')

def common_reseller_login(request):
    return render (request, 'common/reseller_login.html')

def common_reseller_signup(request):
    return render (request, 'common/reseller_signup.html')                