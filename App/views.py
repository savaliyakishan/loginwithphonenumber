from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .manager import *
from .models import *

@login_required(login_url='signin')
def index(request):
    return render(request,'home.html')

def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        phone=request.POST['phone']
        pass1=request.POST['password1']
        pass2=request.POST['password2']

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:
            User.objects.create_user(username=username,phone=phone,password=pass1)
            return redirect('signin')
    return render(request,'signup.html')

def signin(request):
    if request.method=='POST':
        phone=request.POST['phone']
        pass1=request.POST['pass']
        user=authenticate(request,phone=phone,password=pass1)
        if user is not None:
            login(request, user,)
            return redirect('Home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render(request,'signin.html')

def LogoutPage(request):
    logout(request)
    return redirect('signin')