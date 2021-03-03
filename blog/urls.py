from django.urls import path
from .views import *


urlpatterns = [
    path("landing", AdminLandingView.as_view(), name="landing"),
    path("login", AdminLoginView.as_view(), name="login"),
]