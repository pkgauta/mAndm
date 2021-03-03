from django.contrib.auth import login, authenticate
from rest_framework.response import Response
from rest_framework.views import APIView


# noinspection PyMethodMayBeStatic
class LoginAPIView(APIView):

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return Response({"success": True, "message": f"Hola {user.username},\nLogged in successfully!"})

# Create your views here.
