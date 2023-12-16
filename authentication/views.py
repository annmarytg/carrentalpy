from django.shortcuts import render,HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from . models import *
from django.http.response import HttpResponseRedirect

def home(request):
    return render(request, "home.html")

def index(request):
    return render(request, "home.html")
@login_required(login_url='signin')
def base(request):
    return render(request, "base.html")
def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2= request.POST.get('password2')
        
        if pass1 != pass2:
            return HttpResponse("Your password and confirm password are not same!")
        else:
            my_user = User.objects.create_user(username,email,pass1)
            my_user.save()
            return redirect('signin')
        
    return render(request, "signup.html")


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request,username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            return redirect('signup')
        else:
            return HttpResponse("Username or password is incorrect!!!")
    
    return render(request, "signin.html")


def signout(request):
    logout(request)
    return redirect('signin')
def contactus(request):
    return render(request, "contactus.html")
def searchcars(request):
    return render(request, "searchcars.html")
def cart(request):
    return render(request, "cart.html")
def userpage(request):
    return render(request, "userpage.html")

