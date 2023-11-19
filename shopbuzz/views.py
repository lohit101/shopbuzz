from django.shortcuts import render, HttpResponse, redirect
from shopbuzz.forms import UserForm, LoginForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .models import Shop, Product

# Create your views here.
def home(request):
    user = request.user
    shop = Shop.objects.get(shop_owner=user)
    products = Product.objects.filter(prod_owner=shop)
    return HttpResponse(f'You are signed in as {user} <br> Your store name is: {shop} <br> You have the following products in your store: {products} <br> <a href="/accounts/logout/">Log Out</a> <br> <a href="/accounts/login/">Log In</a> <br> <a href="/accounts/signup/">Sign Up</a>')

def about(request):
    return HttpResponse('200 OK/')

def contact(request):
    return HttpResponse('200 OK/')

def inlog(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'GET':
            form = LoginForm()
            return render(request,'inlog.html', {'form': form})
        
        elif request.method == 'POST':
            form = LoginForm(request.POST)
            
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(request,username=username,password=password)
                if user:
                    login(request, user)
                    return redirect('home')
            
            messages.error(request, 'Invalid username or password')
            return render(request,'inlog.html',{'form': form})
  
def upsign(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            form = UserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Account created successfully! You can now log in.')
                return redirect('inlog')
        else:
            form = UserForm()

        return render(request, 'upsign.html', {'form': form})

def outlog(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('inlog') 

def dashboard(request):
    return HttpResponse('200 OK/')

def shop(request):
    return HttpResponse('200 OK/')

def product(request):
    return HttpResponse('200 OK/')

def allproducts(request):
    return HttpResponse('200 OK/')

def settings(request):
    return HttpResponse('200 OK/')