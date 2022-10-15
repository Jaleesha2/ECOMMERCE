from django.urls import path
from . import views

urlpatterns = [
    path('home',views.seller_home),
    path('addproduct',views.seller_addproduct),
    path('updatestock',views.seller_updatestock),
    path('productcatalog',views.seller_productcatalog),
    path('password',views.seller_changepassword)
]