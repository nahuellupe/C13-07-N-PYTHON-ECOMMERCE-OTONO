from django.shortcuts import render, redirect
from .models import Product

def home(request):
    products = Product.objects.all()
    return render(request, "pages/home.html", {"products": products})


def categories(request):
    # Obtener todas las categorías disponibles
    categories = Product.objects.values("category").distinct()

    # Obtener la categoría seleccionada (si se ha enviado en el formulario)
    selected_category = request.GET.get("category")

    # Filtrar los productos según la categoría seleccionada
    if selected_category:
        products = Product.objects.filter(category=selected_category)
    else:
        products = Product.objects.all()

    return render(
        request,
        "pages/categories.html",
        {"categories": categories, "products": products},
    )
