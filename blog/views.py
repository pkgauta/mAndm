from django.shortcuts import render
from django.views.generic import TemplateView


class AdminLandingView(TemplateView):
    template_name = "index.html"


class AdminLoginView(TemplateView):
    template_name = "login.html"


class AdminSignupView(TemplateView):
    template_name = "signup.html"


# Create your views here.
