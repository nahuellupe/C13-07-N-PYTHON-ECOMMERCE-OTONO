from django.urls import path
from . import views

urlpatterns = [
    path("", views.index_view, name="index"),
    path("categories/", views.categories_view, name="categories"),
    path("orders/", views.orders_view, name="orders"),
    path("login/", views.login_view, name="login"),
]
