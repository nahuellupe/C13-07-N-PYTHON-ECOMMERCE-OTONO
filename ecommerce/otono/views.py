from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"


class HomeView(TemplateView):
    template_name = "pages/home.html"


class CategoriesView(TemplateView):
    template_name = "pages/categories.html"


class OrdersView(TemplateView):
    template_name = "pages/orders.html"


class LoginView(TemplateView):
    template_name = "pages/login.html"
