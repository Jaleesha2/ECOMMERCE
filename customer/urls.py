from django.urls import path
from . import views

urlpatterns = [
    path('home',views.customer_home),
    path('product',views.customer_product),
    path('cart',views.customer_cart),
    path('orders',views.customer_myorder),
    path('changepassword',views.customer_changepassword)

   
   
]
