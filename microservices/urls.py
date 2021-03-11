from django.urls import path
from .views import *

urlpatterns = [
    path('login', LoginAPIView.as_view(), name="login"),
    path('add-post', PostAPIView.as_view(), name="add-post")
]