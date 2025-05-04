from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SignupSerializer,UserProfileSerializer,EmployerSerializer
from django.http import HttpResponse
from django.shortcuts import render,redirect
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics, permissions
from .models import Employer
from rest_framework_simplejwt.exceptions import TokenError

User = get_user_model()

class SignupAPIView(APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request):
        return Response({"detail": "GET method not allowed. Use POST to register."},
           status=200 )


def home(request):
    return HttpResponse("""
        <html>
        <head><title>Employer Management System</title></head>
        <body style="font-family: Arial; text-align: center; margin-top: 100px;">
            <h1>Welcome to the Employer Management System API</h1>
            <p>Use the buttons below to register or login.</p>
            <br>
            <a href="/api/auth/signup/" style="padding: 10px 20px; background-color: #4CAF50; color: white; text-decoration: none; border-radius: 5px;">Sign Up</a>
            <a href="/api/auth/login/" style="padding: 10px 20px; background-color: #008CBA; color: white; text-decoration: none; border-radius: 5px; margin-left: 10px;">Login</a>
        </body>
        </html>
    """)

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        return token

class CustomLoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data)


def LoginAPIView(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user:
            login(request, user)
            refresh = RefreshToken.for_user(user)
            request.session['access_token'] = str(refresh.access_token)
            return JsonResponse({"message": "Login successful"})


class EmployerListCreateView(generics.ListCreateAPIView):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer
    permission_classes = [permissions.IsAuthenticated]

class EmployerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer
    permission_classes = [permissions.IsAuthenticated]


class EmployerListCreateView(generics.ListCreateAPIView):
    serializer_class = EmployerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Employer.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class EmployerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EmployerSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        return Employer.objects.filter(user=self.request.user)



class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except TokenError:
            return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
