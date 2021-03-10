from django.urls import path
from .views import *


urlpatterns = [
    path("landing", AdminLandingView.as_view(), name="landing"),
    path("login", AdminLoginView.as_view(), name="login"),
    path("add-post", AdminAddPostView.as_view(), name="add-new-post"),
    path("post-detail", AdminPostDetailView.as_view(), name="post-detail"),
]