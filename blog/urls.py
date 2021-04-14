from django.urls import path
from .views import *


urlpatterns = [
    path("landing", AdminLandingView.as_view(), name="landing"),
    path("login", AdminLoginView.as_view(), name="login"),
    path("add-post", AdminAddPostView.as_view(), name="add-new-post"),
    path("post-list", AdminPostListView.as_view(), name="post-list"),
    path("post-detail/<int:id>", AdminPostDetailView.as_view(), name="post-detail"),
]