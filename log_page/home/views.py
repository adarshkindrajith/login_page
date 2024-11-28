from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages 
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control


# Create your views here.
def index(request):
    return render(request,'index.html')



@never_cache
@login_required(login_url='loginn/')
@cache_control(no_cache=True, no_store=True, must_revalidate=True)
def loginn(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        elif username!=password:
            messages.info(request,'Invalid username or password')
            messages.info(request,'Try again....')
    return render(request,'login.html')

def signup(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']

        myuser=User.objects.create_user(username,email,password)
        myuser.save()
        return redirect('loginn')
    
    return render(request,'signup.html')
    
def home(request):
    return render(request,'home.html')