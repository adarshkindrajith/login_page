from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control

# Create your views here.
def index(request):
    return render(request, 'index.html')

@cache_control(no_cache=True, no_store=True, must_revalidate=True)
def loginn(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid username or password')
    return render(request, 'login.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists. Please choose another one.")
            return redirect('signup')
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered. Please use a different email.")
            return redirect('signup')
        else:
            myuser = User.objects.create_user(username, email, password)
            myuser.save()
            return redirect('loginn')
    
    return render(request, 'signup.html')


@login_required(login_url='loginn')
@cache_control(no_cache=True, no_store=True, must_revalidate=True)
def home(request):
    return render(request, 'home.html')

@login_required(login_url='loginn')
@cache_control(no_cache=True, no_store=True, must_revalidate=True)
def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully!')
    return redirect('loginn')

