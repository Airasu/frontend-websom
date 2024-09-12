from django.shortcuts import render
from django.views.generic import TemplateView

class Home(TemplateView):
    template_name = "pages/home.html"

class Register(TemplateView):
    template_name = "pages/register.html"

class Signin(TemplateView):
    template_name = "pages/signin.html"

class Index(TemplateView):
    template_name = "pages/index.html"

class Announcement(TemplateView):
    template_name = "pages/announcement.html"

class Linked(TemplateView):
    template_name = "pages/linked.html"