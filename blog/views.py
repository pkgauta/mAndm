from django.shortcuts import render
from django.views.generic import TemplateView


class AdminLandingView(TemplateView):
    template_name = "index.html"


class AdminLoginView(TemplateView):
    template_name = "login.html"


class AdminSignupView(TemplateView):
    template_name = "signup.html"


class AdminAddPostView(TemplateView):
    template_name = "add-post.html"


class AdminPostDetailView(TemplateView):
    template_name = "post-detail.html"

# Create your views here.
