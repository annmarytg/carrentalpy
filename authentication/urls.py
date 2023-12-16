from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.index, name='index'),
    path('base/', views.base, name='base'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('contactus/', views.contactus, name='contactus'),
    path('cart/', views.cart, name='cart'),
    path('userpage/', views.userpage, name='userpage'),

   ]
