from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required


def index_view(request):
    return render(request, "index.html")


def home_view(request):
    products = Product.objects.all()
    return render(request, "pages/home.html")


def orders_view(request):
    return render(request, "pages/orders.html")


def login_view(request):
    return render(request, "pages/login.html")


def categories_view(request):
    return render(request, "pages/categories.html")
