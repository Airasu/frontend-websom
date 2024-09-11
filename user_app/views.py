from django.shortcuts import render
from django.views.generic import TemplateView

class Home(TemplateView):
    template_name = "pages/home.html"

class Register(TemplateView):
    template_name = "pages/register.html"

class Register2(TemplateView):
    template_name = "pages/register2.html"

class Signin(TemplateView):
    template_name = "pages/signin.html"

class Dashboard(TemplateView):
    template_name = "pages/dashboard.html"

class Index(TemplateView):
    template_name = "pages/index.html"


