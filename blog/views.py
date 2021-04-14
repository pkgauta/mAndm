from django.shortcuts import render
from .utils import get_choices_for_pages
from django.views.generic import TemplateView


class AdminLandingView(TemplateView):
    template_name = "index.html"


class AdminLoginView(TemplateView):
    template_name = "login.html"


class AdminSignupView(TemplateView):
    template_name = "signup.html"


class AdminAddPostView(TemplateView):
    template_name = "add-post.html"

    def get_context_data(self, **kwargs):
        context = super(AdminAddPostView, self).get_context_data(**kwargs)
        context["choices"] = get_choices_for_pages("add-post")
        return context


class AdminPostListView(TemplateView):
    template_name = "post.html"


class AdminPostDetailView(TemplateView):
    template_name = "post-detail.html"

# Create your views here.
