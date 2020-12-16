from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'signup.html')
def signup(request):
    if request.method=='POST':
        email=request.POST.get('email')
        name=request.POST.get('name')
        password=request.POST.get('password')
        usercheck=User.objects.filter(username=name)
        if usercheck:
            messages.error(request,"User already exists with this username")
            return redirect('/')
        userobj=User.objects.create_user(first_name=name,password=password,email=email,username=name)
        userobj.save()
        
    return redirect('/')
def user_login(request):
    if request.method=='POST':
        name=request.POST.get('name')
        password=request.POST.get('password')
        user=authenticate(username=name,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"Logged in")
            return redirect('/userpage')
        else:
            messages.error(request,"Invalid credentials")
            return redirect('/')
def user_logout(request):
    logout(request)
    messages.success(request,"Logged Out")
    return redirect('/')