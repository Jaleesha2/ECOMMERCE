from django.urls import path
from . import views

urlpatterns = [
    path('customer_login',views.common_customer_login, name='cus_login'),
    path('customer_signup',views.common_customer_signup, name='cus_signin'),
    path('project_home',views.common_project_home, name='project_home'),
    path('reseller_login',views.common_reseller_login, name='reseller_login'),
    path('reseller_signup',views.common_reseller_signup, name='reseller_signin')

   
]