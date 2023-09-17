from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("categories/", views.CategoriesView.as_view(), name="categories"),
    path("orders/", views.OrdersView.as_view(), name="orders"),
    path("login/", views.LoginView.as_view(), name="login"),
]
