from django.urls import path
from .views import Home, Register, Signin, Index, Announcement, Linked 

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("register", Register.as_view(), name="Register"),
    path("signin", Signin.as_view(), name="Signin"),
    path("index", Index.as_view(), name="Index"),
    path("announcement", Announcement.as_view(), name="Announcement"),
    path("linked", Linked.as_view(), name="Linked")
]
