from django.shortcuts import render
from django.contrib.auth import authenticate


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken



from .serializers import UserSerializer
from .models import User

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        # Authenticate user
        user = authenticate(username=username, password=password)

        # If authentication is successful, generate JWT token
        if user is not None:
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)

            return Response({
                'access': access_token,
                'refresh': refresh_token
            }, status=status.HTTP_200_OK)

        return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)