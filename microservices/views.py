from blog.models import *
from .serializers import *
from rest_framework import mixins
from django.core import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import login, authenticate
# noinspection PyMethodMayBeStatic
from blog.utils import check_mandate
from microservices.utils import create_blog_images_object


class LoginAPIView(APIView):

    def post(self, request):
        if "username" and "password" in request.POST:
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return Response({"success": True, "message": f"Hola {user.username},\nLogged in successfully!"})
            else:
                return Response({"success": False, "message": "Invalid credentials !"})
        else:
            return Response({"success": False, "message": "Username and Password are mandatory !"})


class PostAPIView(APIView, mixins.ListModelMixin):

    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    def get(self, request, id=None):
        if id is not None:
            response = self.queryset.filter(id=id)
        else:
            response = serializers.serialize('json', self.queryset.all().prefetch_related('post_image'))
        return Response({"success": True, "data": response,  "message": "List fetched successfully !"})

    def post(self, request):
        try:
            mandate_fields = {"title", "status", "category", "description"}
            params = {}
            for data in request.POST.keys():
                params[data] = request.POST.get(data)
            if mandate_fields <= request.POST.keys():
                image_ids = create_blog_images_object(request.FILES)
                post_obj = BlogPost.objects.create(**params)
                post_obj.post_image.add(*image_ids)
                post_obj.author = request.user
                post_obj.save()
                request.POST._mutable = False
            return Response({"success": True, "message": "Post added successfully !"})
        except Exception as error:
            return Response({"success": False, "message": "Something bad happened !"})

# Create your views here.
