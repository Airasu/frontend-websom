from django.urls import path
from .views import Home, Register, Signin, Dashboard, Index

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("register", Register.as_view(), name="Register"),
    path("signin", Signin.as_view(), name="Signin"),
    path("dashboard", Dashboard.as_view(), name="Dashboard"),
    path("index", Index.as_view(), name="Index"),
]
