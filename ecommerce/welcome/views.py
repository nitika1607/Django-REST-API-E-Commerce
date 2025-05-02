from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product
from .serializers import ProductSerializer
from rest_framework import status
from django.shortcuts import render, get_object_or_404
import requests


@api_view(['GET'])
def product_list_api(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def product_detail_api(request, pk):
    product = get_object_or_404(Product, pk=pk)
    serializer = ProductSerializer(product)
    return Response(serializer.data)

def index(request):
    carousel_item = {
        'title': 'Beauty <br> kit',
        'description': 'Ncididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo',
        'button': 'Buy Now',
        'image': '/images/banner-img.png',
    }
    carousel_images = [carousel_item] * 3  # repeat same slide 3 times

    # Fetch all products from the database
    product_list = Product.objects.all()
    
    return render(request, 'index.html', {
        'carousel_images': carousel_images,
        'product_list': product_list
    })

def product_page(request):
    products = Product.objects.all()  # Fetch directly from the database
    return render(request, 'product_page.html', {'products': products})

#Fetching product details
def product_detail(request, id):
    # Fetch product by ID
    product = get_object_or_404(Product, id=id)
    return render(request, 'product_detail.html', {'product': product})


def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def client(request):
    return render(request, 'client.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/welcome/')
        else:
            return render(request, 'login.html', {'form' : {'error': True}})
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            return render(request, 'register.html', {'error': "Password do not match"})
        
        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': "Username already exists"})
        
        if User.objects.filter(email=email).exists():
            return render(request, 'register.html', {'error' : "Email is already exsits"})
        
        user = User.objects.create_user(username=username ,email=email, password=password1)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        login(request, user)
        return redirect("/")
    return render(request, 'register.html')
