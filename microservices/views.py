from django.contrib.auth import login, authenticate
from rest_framework.response import Response
from blog.models import *
from rest_framework.views import APIView


# noinspection PyMethodMayBeStatic
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


class PostAPIView(APIView):

    def post(self, request):
        
        import pdb; pdb.set_trace()

# Create your views here.
